import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

import datetime

from django.utils import timezone

from webpagetester.models import User, Application, Test
from webpagetester.utils import WebPageTester


make_users = False
make_apps = False

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
else:
    app = Application.objects.get(pk=3)

dia = datetime.datetime.today().day
mes = datetime.datetime.today().month
for i in range(5):
    test = Test(label='Test {app} {dia}_{mes}_{num}'.format(app=app.name , num=i+1, dia=dia, mes=mes),
                application=app,
                url='www.pontofrio.com.br',
                created_date=timezone.now(),
                created_by=user)
    print('Creating test {test}'.format(test=test.label))
    test.save()
    wpt = WebPageTester()
    wpt.create_test(test)
