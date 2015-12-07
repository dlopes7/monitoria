import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

import datetime
import time

from django.utils import timezone

from webpagetester.models import User, Application, Test
from webpagetester.utils import WebPageTester


make_users = False
make_apps = False

app_names = ['Extra',
             'Casas Bahia',
             'Ponto Frio']

if make_users:
    print('Creating user David')
    user = User(name='David')
    user.save()
else:
    user = User.objects.get(pk=1)

if make_apps:
    print('Creating app Extra')
    app = Application(name='Extra')
    app.save()

i = 0

while True:
    dia = datetime.datetime.today().day
    mes = datetime.datetime.today().month

    for app_name in app_names:
        app = Application.objects.get(name=app_name)
        test = Test(label='Test {app} {dia}_{mes}_{num}'.format(app=app.name , num=i+1, dia=dia, mes=mes),
                    application=app,
                    url='www.{bandeira}.com.br'.format(bandeira=app_name.lower().replace(' ', '')),
                    created_date=timezone.now(),
                    created_by=user)
        print('Creating test {test}'.format(test=test.label))
        test.save()
        wpt = WebPageTester()
        wpt.create_test(test)

    i+= 1
    time.sleep(3600)
