import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

from django.utils import timezone

from webpagetester.models import User, Application, Test
from webpagetester.utils import WebPageTester

print('Creating user David')
user = User(name='David')
user.save()

print('Creating app Extra')
app = Application(name='Extra')
app.save()

for i in range(5):
    test = Test(label='Test {app} {num}'.format(app=app.name , num=i+1),
                application=app,
                url='www.extra.com.br',
                created_date=timezone.now(),
                created_by=user)
    print('Creating test {test}'.format(test=test.label))
    test.save()
    wpt = WebPageTester()
    wpt.create_test(test)
