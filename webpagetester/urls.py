from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<app_id>[0-9]+)/$', views.app_detail, name='app_detail'),
    url(r'^create_test/$', views.create_test, name='create_test'),

]