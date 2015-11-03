import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoria.settings")

from webpagetester.utils import WebPageTester

wpt = WebPageTester()

wpt.check_if_test_complete(test_id='13456')
