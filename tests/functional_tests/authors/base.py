from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.tests.selenium.browser import make_chrome_driver


class SeleniumBaseTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = make_chrome_driver()

        return super().setUp()

    def tearDown(self):
        self.browser.quit()