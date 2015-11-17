from django.utils import timezone

from django.db import models

class Log(models.Model):
    date = models.DateTimeField('created date', default=timezone.now())
    entry = models.CharField(max_length=1000)

class User(models.Model):
    name = models.CharField(max_length=200)


class Application(models.Model):
    name = models.CharField(max_length=200, unique=True)


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
    wpt_from = models.CharField(max_length=200, default='placeholder')
    wpt_location = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_SpeedIndex = models.IntegerField(default=0)
    wpt_firstView_TTFB =models.IntegerField(default=0)
    wpt_firstView_base_page_cdn = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_css_bytes = models.IntegerField(default=0)
    wpt_firstView_breakdown_css_color = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_css_requests = models.IntegerField(default=0)
    wpt_firstView_breakdown_flash_bytes = models.IntegerField(default=0)
    wpt_firstView_breakdown_flash_color = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_flash_requests = models.IntegerField(default=0)
    wpt_firstView_breakdown_html_bytes = models.IntegerField(default=0)
    wpt_firstView_breakdown_html_color = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_html_requests = models.IntegerField(default=0)
    wpt_firstView_breakdown_image_bytes = models.IntegerField(default=0)
    wpt_firstView_breakdown_image_color = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_image_requests = models.IntegerField(default=0)
    wpt_firstView_breakdown_js_bytes = models.IntegerField(default=0)
    wpt_firstView_breakdown_js_color = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_js_requests = models.IntegerField(default=0)
    wpt_firstView_breakdown_other_bytes = models.IntegerField(default=0)
    wpt_firstView_breakdown_other_color = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_breakdown_other_requests = models.IntegerField(default=0)
    wpt_firstView_bytesIn = models.IntegerField(default=0)
    wpt_firstView_bytesInDoc = models.IntegerField(default=0)
    wpt_firstView_bytesOut = models.IntegerField(default=0)
    wpt_firstView_bytesOutDoc = models.IntegerField(default=0)
    wpt_firstView_cached = models.IntegerField(default=0)
    wpt_firstView_connections = models.IntegerField(default=0)
    wpt_firstView_date = models.IntegerField(default=0)
    wpt_firstView_docCPUms = models.IntegerField(default=0)
    wpt_firstView_docCPUpct = models.IntegerField(default=0)
    wpt_firstView_docTime = models.IntegerField(default=0)
    wpt_firstView_gzip_savings = models.IntegerField(default=0)
    wpt_firstView_gzip_total = models.IntegerField(default=0)
    wpt_firstView_image_savings = models.IntegerField(default=0)
    wpt_firstView_image_total = models.IntegerField(default=0)
    wpt_firstView_lastVisualChange = models.IntegerField(default=0)
    wpt_firstView_loadTime = models.IntegerField(default=0)
    wpt_firstView_render = models.IntegerField(default=0)
    wpt_firstView_requests = models.IntegerField(default=0)
    wpt_firstView_responses_200 = models.IntegerField(default=0)
    wpt_firstView_responses_404 = models.IntegerField(default=0)
    wpt_firstView_responses_other = models.IntegerField(default=0)
    wpt_firstView_score_cache = models.IntegerField(default=0)
    wpt_firstView_score_cdn = models.IntegerField(default=0)
    wpt_firstView_score_combine = models.IntegerField(default=0)
    wpt_firstView_score_compress = models.IntegerField(default=0)
    wpt_firstView_score_cookies = models.IntegerField(default=0)
    wpt_firstView_score_etags = models.IntegerField(default=0)
    wpt_firstView_score_gzip = models.IntegerField(default=0)
    wpt_firstView_score_keep_alive = models.IntegerField(default=0)
    wpt_firstView_score_minify = models.IntegerField(default=0)
    wpt_firstView_score_progressive_jpeg = models.IntegerField(default=0)
    wpt_firstView_server_count = models.IntegerField(default=0)
    wpt_firstView_server_rtt = models.IntegerField(default=0)
    wpt_firstView_tester = models.CharField(max_length=200, default='placeholder')
    wpt_firstView_images_screenShot = models.CharField(max_length=300, default='placeholder')


    def update_from_test_result(self, test_result):
        self.wpt_status_code = test_result['statusCode']
        self.wpt_status_text = test_result['statusText']

        #If the test completed without errors
        if self.wpt_status_code == 200:



            self.wpt_from = test_result['data']['from']
            self.wpt_location = test_result['data']['location']

            if test_result['data']['runs']['1']['firstView'] is not None:
                self.wpt_firstView_SpeedIndex = test_result['data']['runs']['1']['firstView']['SpeedIndex']
                self.wpt_firstView_TTFB = test_result['data']['runs']['1']['firstView']['TTFB']
                self.wpt_firstView_base_page_cdn = test_result['data']['runs']['1']['firstView']['base_page_cdn']
                self.wpt_firstView_breakdown_css_bytes = test_result['data']['runs']['1']['firstView']['breakdown']['css']['bytes']
                self.wpt_firstView_breakdown_css_color = test_result['data']['runs']['1']['firstView']['breakdown']['css']['color']
                self.wpt_firstView_breakdown_css_requests = test_result['data']['runs']['1']['firstView']['breakdown']['css']['requests']
                self.wpt_firstView_breakdown_flash_bytes = test_result['data']['runs']['1']['firstView']['breakdown']['flash']['bytes']
                self.wpt_firstView_breakdown_flash_color = test_result['data']['runs']['1']['firstView']['breakdown']['flash']['color']
                self.wpt_firstView_breakdown_flash_requests = test_result['data']['runs']['1']['firstView']['breakdown']['flash']['requests']
                self.wpt_firstView_breakdown_html_bytes = test_result['data']['runs']['1']['firstView']['breakdown']['html']['bytes']
                self.wpt_firstView_breakdown_html_color = test_result['data']['runs']['1']['firstView']['breakdown']['html']['color']
                self.wpt_firstView_breakdown_html_requests = test_result['data']['runs']['1']['firstView']['breakdown']['html']['requests']
                self.wpt_firstView_breakdown_image_bytes = test_result['data']['runs']['1']['firstView']['breakdown']['image']['bytes']
                self.wpt_firstView_breakdown_image_color = test_result['data']['runs']['1']['firstView']['breakdown']['image']['color']
                self.wpt_firstView_breakdown_image_requests = test_result['data']['runs']['1']['firstView']['breakdown']['image']['requests']
                self.wpt_firstView_breakdown_js_bytes = test_result['data']['runs']['1']['firstView']['breakdown']['js']['bytes']
                self.wpt_firstView_breakdown_js_color = test_result['data']['runs']['1']['firstView']['breakdown']['js']['color']
                self.wpt_firstView_breakdown_js_requests = test_result['data']['runs']['1']['firstView']['breakdown']['js']['requests']
                self.wpt_firstView_breakdown_other_bytes = test_result['data']['runs']['1']['firstView']['breakdown']['other']['bytes']
                self.wpt_firstView_breakdown_other_color = test_result['data']['runs']['1']['firstView']['breakdown']['other']['color']
                self.wpt_firstView_breakdown_other_requests = test_result['data']['runs']['1']['firstView']['breakdown']['other']['requests']
                self.wpt_firstView_bytesIn = test_result['data']['runs']['1']['firstView']['bytesIn']
                self.wpt_firstView_bytesInDoc = test_result['data']['runs']['1']['firstView']['bytesInDoc']
                self.wpt_firstView_bytesOut = test_result['data']['runs']['1']['firstView']['bytesOut']
                self.wpt_firstView_bytesOutDoc = test_result['data']['runs']['1']['firstView']['bytesOutDoc']
                self.wpt_firstView_cached = test_result['data']['runs']['1']['firstView']['cached']
                self.wpt_firstView_connections = test_result['data']['runs']['1']['firstView']['connections']
                self.wpt_firstView_date = test_result['data']['runs']['1']['firstView']['date']
                self.wpt_firstView_docCPUms = test_result['data']['runs']['1']['firstView']['docCPUms']
                self.wpt_firstView_docCPUpct = test_result['data']['runs']['1']['firstView']['docCPUpct']
                self.wpt_firstView_docTime = test_result['data']['runs']['1']['firstView']['docTime']
                self.wpt_firstView_gzip_savings = test_result['data']['runs']['1']['firstView']['gzip_savings']
                self.wpt_firstView_gzip_total = test_result['data']['runs']['1']['firstView']['gzip_total']
                self.wpt_firstView_image_savings = test_result['data']['runs']['1']['firstView']['image_savings']
                self.wpt_firstView_image_total = test_result['data']['runs']['1']['firstView']['image_total']
                self.wpt_firstView_lastVisualChange = test_result['data']['runs']['1']['firstView']['lastVisualChange']
                self.wpt_firstView_loadTime = test_result['data']['runs']['1']['firstView']['loadTime']
                self.wpt_firstView_render = test_result['data']['runs']['1']['firstView']['render']
                self.wpt_firstView_requests = test_result['data']['runs']['1']['firstView']['requests']
                self.wpt_firstView_responses_200 = test_result['data']['runs']['1']['firstView']['responses_200']
                self.wpt_firstView_responses_404 = test_result['data']['runs']['1']['firstView']['responses_404']
                self.wpt_firstView_responses_other = test_result['data']['runs']['1']['firstView']['responses_other']
                self.wpt_firstView_score_cache = test_result['data']['runs']['1']['firstView']['score_cache']
                self.wpt_firstView_score_cdn = test_result['data']['runs']['1']['firstView']['score_cdn']
                self.wpt_firstView_score_combine = test_result['data']['runs']['1']['firstView']['score_combine']
                self.wpt_firstView_score_compress = test_result['data']['runs']['1']['firstView']['score_compress']
                self.wpt_firstView_score_cookies = test_result['data']['runs']['1']['firstView']['score_cookies']
                self.wpt_firstView_score_etags = test_result['data']['runs']['1']['firstView']['score_etags']
                self.wpt_firstView_score_gzip = test_result['data']['runs']['1']['firstView']['score_gzip']
                self.wpt_firstView_score_keep_alive = test_result['data']['runs']['1']['firstView']['score_keep-alive']
                self.wpt_firstView_score_minify = test_result['data']['runs']['1']['firstView']['score_minify']
                self.wpt_firstView_score_progressive_jpeg = test_result['data']['runs']['1']['firstView']['score_progressive_jpeg']
                self.wpt_firstView_server_count = test_result['data']['runs']['1']['firstView']['server_count']
                self.wpt_firstView_server_rtt = test_result['data']['runs']['1']['firstView']['server_rtt']
                self.wpt_firstView_tester = test_result['data']['runs']['1']['firstView']['tester']
                self.wpt_firstView_images_screenShot = test_result['data']['runs']['1']['firstView']['images']['screenShot']
            else:
                self.wpt_status_code = -1
                self.wpt_status_text = 'Error executing test'



        #If tested is still not completed, some data is in different places on the json return
        elif self.wpt_status_code > 100 and self.wpt_status_code < 200:
            self.wpt_from = test_result['data']['testInfo']['browser']
            self.wpt_location = test_result['data']['testInfo']['location']

        self.save()





