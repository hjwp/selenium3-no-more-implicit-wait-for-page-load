import unittest
from selenium import webdriver
import subprocess

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class QuickTest(unittest.TestCase):
    def setUp(self):
        server = subprocess.Popen(
            ['python', '-m', 'http.server', '8101']
        )
        self.addCleanup(server.kill)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.addCleanup(self.driver.quit)


    def test_clicking_around_fast(self):
        self.driver.get('http://localhost:8101')
        for _ in range(100):
            self.assertEqual(
                self.driver.find_element_by_tag_name('h1').text,
                'Index page'
            )
            self.driver.find_element_by_css_selector('#page2').click()
            self.assertEqual(
                self.driver.find_element_by_tag_name('h1').text,
                'Page 2'
            )
            self.driver.find_element_by_link_text('page 3').click()
            self.assertEqual(
                self.driver.find_element_by_tag_name('h1').text,
                'Page 3'
            )
            self.driver.find_element_by_link_text('index page').click()


if __name__ == '__main__':
    unittest.main()

