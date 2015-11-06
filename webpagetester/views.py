from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q

from django_tables2 import RequestConfig

from .models import Application, Test, User
from .forms import TestForm
from .utils import WebPageTester
from .tables import TestTable

def index(request):
    applications = Application.objects.all()
    dict_apps = {}
    for app in applications:
        num_tests_completed = len(Test.objects.filter(wpt_status_code = 200, application=app))
        num_tests_not_completed = len(Test.objects.filter(~Q(wpt_status_code = 200), application=app))

        dict_apps[app.name] = {'id':app.id,
                               'completed': num_tests_completed,
                               'not_completed': num_tests_not_completed}

    print(dict_apps)
    return render(request, 'index.html', {'applications': dict_apps,
                                          })


def app_detail(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    tests = Test.objects.filter(application=app)

    table = TestTable(tests)
    RequestConfig(request).configure(table)

    return render(request, 'app_detail.html', {'table': table, 'app':app})

def update_test(request):

    id_teste = request.POST['test_id']
    test = Test.objects.get(id=int(id_teste))
    wpt = WebPageTester()
    print('Updating Test "{id} - {name}"'.format(id=test.id ,name=test.label))
    test.update_from_test_result(wpt.get_test_details(test.wpt_test_id))

    return HttpResponse('OK')


def create_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            test_label = form.cleaned_data['test_label']
            test_url = form.cleaned_data['test_url']
            test_application = form.cleaned_data['test_application']

            test_created_date = timezone.now()
            test_user = User.objects.get(id=1)
            test_app = Application.objects.get(id=test_application)

            test = Test(label=test_label,
                        application=test_app,
                        url=test_url,
                        created_date=test_created_date,
                        created_by=test_user)

            test.save()

            wpt = WebPageTester()
            wpt.create_test(test)

            return render(request, 'test_created.html', {'test': test})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'create_test.html', {'form': form})