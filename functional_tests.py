import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = True
        caps['binary'] = '/usr/bin/firefox'
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('To-Do', self.browser.title)

if __name__ == '__main__':
    unittest.main()
