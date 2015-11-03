from django.utils import timezone

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)


class Application(models.Model):
    name = models.CharField(max_length=200)


class Test(models.Model):
    label = models.CharField(max_length=200)
    application = models.ForeignKey(Application)
    created_by = models.ForeignKey(User)
    created_date = models.DateTimeField('created date', default=timezone.now())
    url = models.CharField(max_length=1000)

    wpt_status_code = models.IntegerField(default=200)
    wpt_status_text = models.CharField(max_length=100, default='placeholder')
    wpt_test_id = models.CharField(max_length=100, default='placeholder')
    wpt_jsonUrl = models.CharField(max_length=200, default='placeholder')
    wpt_userUrl = models.CharField(max_length=200, default='placeholder')




