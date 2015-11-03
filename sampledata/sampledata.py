import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

from webpagetester.models import User, Application

user = User(name='David')
user.save()
app = Application(name='Extra')
app.save()

