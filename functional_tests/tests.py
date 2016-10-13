from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        # https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver
        caps = DesiredCapabilities.FIREFOX
        caps['marionette'] = True
        caps['binary'] = '/usr/bin/firefox'
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        self._check_for_row_in_list_table(
            '1: Buy peacock feathers'
        )
        self._check_for_row_in_list_table(
            '1: Buy peacock feathers'
        )
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        self._check_for_row_in_list_table(
            '1: Buy peacock feathers'
        )
        self._check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
        )

    def _check_for_row_in_list_table(self, row_text):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.ID, 'id_list_table')
            )
        )
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, 'tr')
            )
        )
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
