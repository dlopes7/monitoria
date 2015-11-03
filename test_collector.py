import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

from webpagetester.utils import WebPageTester
from django.db.models import Q

from webpagetester.models import User, Application, Test


wpt = WebPageTester()
tests_not_completed = Test.objects.filter(~Q(wpt_status_code = 200))

for test in tests_not_completed:
    print (test.wpt_status_code, test.wpt_status_text, end=' -> ')

    json_result = wpt.get_test_details(test.wpt_test_id)
    test.update_from_test_result(json_result)

    print (test.wpt_status_code, test.wpt_status_text)


#TODO
'''
Gotta populate all the test results that will be used later
This will probably be gotten from the ['data']['average']['firstView']
and ['data']['average']['repeatView']
and ['data']['runs']['1']['firstView']
REMEMBER - This is done at the Model level, not here!
'''