import unittest
from selenium import webdriver
import subprocess


class QuickTest(unittest.TestCase):
    def setUp(self):
        server = subprocess.Popen(
            ['python', 'flask_app.py']
        )
        self.addCleanup(server.kill)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.addCleanup(self.driver.quit)


    def test_clicking_around_fast(self):
        self.driver.get('http://localhost:5000/page/1')
        for i in range(1, 21):
            print('loop', i)
            self.assertEqual(
                self.driver.find_element_by_tag_name('h1').text,
                'Page 1'
            )
            # self.driver.find_element_by_css_selector('#page2').click()
            self.driver.find_element_by_link_text('page 2').click()
            self.assertEqual(
                self.driver.find_element_by_tag_name('h1').text,
                'Page 2'
            )
            self.driver.find_element_by_link_text('page 3').click()
            self.assertEqual(
                self.driver.find_element_by_tag_name('h1').text,
                'Page 3'
            )
            # self.driver.find_element_by_link_text('index page').click()
            self.driver.find_element_by_link_text('page 1').click()


if __name__ == '__main__':
    unittest.main()

