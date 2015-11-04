from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Application, Test, User
from .forms import TestForm
from .utils import WebPageTester
from .tables import TestTable

def index(request):
    applications = Application.objects.all()
    return render(request, 'index.html', {'applications': applications,
                                          })


def app_detail(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    tests = Test.objects.filter(application=app)

    table = TestTable(tests)

    return render(request, 'app_detail.html', {'table': table})


def create_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            test_label = form.cleaned_data['test_label']
            test_url = form.cleaned_data['test_url']
            test_created_date = timezone.now()
            test_user = User.objects.get(id=1)
            test_app = Application.objects.get(id=1)

            test = Test(label=test_label,
                        application=test_app,
                        url=test_url,
                        created_date=test_created_date,
                        created_by=test_user)


            wpt = WebPageTester()
            json_result = (wpt.create_test(url=test.url, label=test.label))

            test.wpt_test_id = json_result['data']['testId']
            test.wpt_jsonUrl = json_result['data']['jsonUrl']
            test.wpt_userUrl = json_result['data']['userUrl']

            test.save()

            json_test_result = wpt.get_test_details(test.wpt_test_id)
            test.update_from_test_result(json_test_result)

            return render(request, 'test_created.html', {'test': test})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'create_test.html', {'form': form})