import requests

from monitoria.config import WPT_FORMAT, WPT_KEY, WPT_PASSWORD, WPT_LOGIN

class WebPageTester:
    def create_test(self, url, label):
        url_wpt = 'http://www.webpagetest.org/runtest.php?'
        params = {
            'url': url,
            'label': label,
            'f': WPT_FORMAT,
            'login': WPT_LOGIN,
            'password': WPT_PASSWORD,
            'k': WPT_KEY,
        }
        r = requests.get(url_wpt, params=params)
        return r.json()

    def check_if_test_complete(self, test_id):
        print('Vaza anta ' + test_id)

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




