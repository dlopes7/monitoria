import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

from webpagetester.utils import WebPageTester
from django.db.models import Q

from webpagetester.models import User, Application, Test


wpt = WebPageTester()

while True:
    tests_not_completed = Test.objects.filter(~Q(wpt_status_code = 200), ~Q(wpt_status_code = -1))

    for test in tests_not_completed:
        try:
            print (test.label, test.wpt_status_code, test.wpt_status_text, end=' -> ')

            json_result = wpt.get_test_details(test.wpt_test_id)
            test.update_from_test_result(json_result)

            print (test.wpt_status_code, test.wpt_status_text)
        except:
            pass

    time.sleep(5 * 60)

