import json
from datetime import datetime
from django.core import serializers
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import timezone
from django.db.models import Q
from django_tables2 import RequestConfig
from .models import Application, Test, User, Log, Metric
from .forms import TestForm
from .utils import WebPageTester
from .tables import TestTable


def index(request):
    '''

    Home Page
    has the application list and the number of completed/incompleted tests on each
    :param request:
    :return:
    '''
    applications = Application.objects.all()
    dict_apps = {}
    for app in applications:
        num_tests_completed = len(Test.objects.filter(wpt_status_code=200, application=app))
        num_tests_not_completed = len(Test.objects.filter(~Q(wpt_status_code=200), application=app))

        dict_apps[app] = {'id': app.id,
                          'completed': num_tests_completed,
                          'not_completed': num_tests_not_completed}

    print(dict_apps)
    return render(request, 'index.html', {'applications': dict_apps,
                                          })

def app_detail(request, app_id):
    '''

    Tests management page
    Has a table with all the tests and buttons to create, compare, delete tests
    :param request:
    :param app_id: ID of the app the user wants to see
    :return:
    '''
    app = get_object_or_404(Application, pk=app_id)
    tests = Test.objects.filter(application=app)

    table = TestTable(tests)
    RequestConfig(request).configure(table)

    return render(request, 'app_detail.html', {'table': table, 'app': app})


def update_test(request):
    '''

    Calls the WebPageTester API to update the test
    This should be a POST with the parameter test_id sent
    :param request:
    :return:
    '''

    id_teste = request.POST['test_id']
    test = Test.objects.get(id=int(id_teste))
    wpt = WebPageTester()
    print('Updating Test "{id} - {name}"'.format(id=test.id, name=test.label))
    test.update_from_test_result(wpt.get_test_details(test.wpt_test_id))

    return HttpResponse('OK')


def app_chart(request):
    """
    Simple view to render the app chart page
    :param request: The web request
    :return: The template rendered with the list of apps
    """
    apps = Application.objects.all()
    metrics = Metric.objects.all()
    return render(request, 'app_chart.html', {'apps': apps})


def get_metric_description(request):
    """
    Little webservice to get the description of a Metric object
    :return: JSON response containing the metric description in Portuguese
    """
    metric = request.GET['metric']

    metric = Metric.objects.get(metric_id=metric)
    metric_json = {metric.metric_id: metric.description_ptBR}

    return HttpResponse(json.dumps(metric_json), content_type="application/json")


def json_chart(request):
    try:
        app_id = request.GET['app_id']
        metric = request.GET['metric']
        # url = request.GET['url']
        time_from = request.GET['time_from']
        time_to = request.GET['time_to']

        print(time_from, time_to)
        time_from_formatted = datetime.strptime(time_from, "%d/%m/%Y %H:%M:%S")
        time_to_formatted = datetime.strptime(time_to, "%d/%m/%Y %H:%M:%S")

        app = Application.objects.get(pk=app_id)
        tests = Test.objects.filter(application=app,
                                    created_date__gt=time_from_formatted,
                                    created_date__lt=time_to_formatted,
                                    wpt_status_code=200,
                                    # url=url,
                                    ).order_by('created_date')

        data = serializers.serialize('json',
                                     tests,
                                     fields=('label', 'created_date', metric, 'url'),
                                     )

    except Exception as e:
        return HttpResponseBadRequest('Error: ' + str(e))

    return HttpResponse(data, content_type='application/javascript')


def create_test(request):
    '''

    GET - Return the create test page
    POST - creates the test. POST should have the parameters 'test_label', 'test_url' and 'test_application'
    :param request:
    :return:
    '''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            test_label = form.cleaned_data['test_label']
            test_url = form.cleaned_data['test_url']
            test_application = form.cleaned_data['test_application']

            user = User.objects.get(id=1)

            test = Test(label=test_label,
                        application=Application.objects.get(id=test_application),
                        url=test_url,
                        created_date=timezone.now(),
                        created_by=user)
            test.save()
            log = Log(date=timezone.now(),
                      entry='{usuario} - Test {id} criado - {url}'.format(id=test.id, usuario=user.name, url=test_url))
            log.save()

            wpt = WebPageTester()
            wpt.create_test(test)

            return render(request, 'test_created.html', {'test': test})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'create_test.html', {'form': form})


def delete_tests(request):
    """

    :param request: The web request, should contain a paremeter 'tests'
    :return: OK, the alerts have been deleted
    """
    id_tests = request.POST['tests'].split(';')
    for id_test in id_tests:
        print('Deleting test ID {id}'.format(id=id_test))
        test = Test.objects.get(id=int(id_test))
        test.delete()
        log = Log(date=timezone.now(),
                  entry='{usuario} - Test {id} deletado - {url}'.format(id=id_test, usuario='Teste', url=test.url))
        log.save()

    return HttpResponse('OK')
