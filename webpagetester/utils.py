import requests

from monitoria.config import WPT_FORMAT, WPT_KEY, WPT_PASSWORD, WPT_LOGIN
from webpagetester.models import Test

class WebPageTester:
    def create_test(self, test):
        url_wpt = 'http://www.webpagetest.org/runtest.php?'
        params = {
            'url': test.url,
            'label': test.label,
            #'location': 'ec2-sa-east-1:Chrome',
            'f': WPT_FORMAT,
            'login': WPT_LOGIN,
            'password': WPT_PASSWORD,
            'k': WPT_KEY,
        }
        r = requests.get(url_wpt, params=params)
        json_result = r.json()

        test.wpt_status_code = json_result['statusCode']
        test.wpt_status_text = json_result['statusText']

        if test.wpt_status_code > 300:
            print(json_result)
            return None
        else:
            test.wpt_test_id = json_result['data']['testId']
            test.wpt_jsonUrl = json_result['data']['jsonUrl']
            test.wpt_userUrl = json_result['data']['userUrl']

        test.save()
        test.update_from_test_result(self.get_test_details(test.wpt_test_id))

    def get_test_details(self, test_id):
        url_wpt = 'http://www.webpagetest.org/jsonResult.php?'
        params = {
            'requests':0,
            'domains':1,
            'breakdown':1,
            'test':test_id,
        }
        r = requests.get(url_wpt, params=params)
        return r.json()

def ms_to_sec(ms):
    return int(ms)/1000

def size(bytes):
    system = [
		(1024 ** 5, 'P'),
		(1024 ** 4, 'T'),
		(1024 ** 3, 'G'),
		(1024 ** 2, 'M'),
		(1024 ** 1, 'K'),
		(1024 ** 0, 'B'),
		]

    for factor, suffix in system:
        if bytes >= factor:
            break

    amount = int(bytes/factor)
    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple

    return str(amount) + suffix


