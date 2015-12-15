from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<app_id>[0-9]+)/$', views.app_detail, name='app_detail'),
    url(r'^charts/$', views.app_chart, name='app_chart'),
    url(r'^create_test/$', views.create_test, name='create_test'),
    url(r'^update_test/$', views.update_test, name='update_test'),
    url(r'^delete_tests/$', views.delete_tests, name='delete_tests'),

    url(r'^json_chart/$', views.json_chart, name='json_chart'),
    url(r'^get_metric_description/$', views.get_metric_description, name='get_metric_description'),

    #get_metric_description
]