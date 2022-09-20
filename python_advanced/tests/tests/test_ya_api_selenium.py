import unittest
from selenium import webdriver
from Netology.python_advanced.tests.ya_api_selenium import get_password
from time import sleep


class YaPassportSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_authorization(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        elem = driver.find_element(by='css selector', value='div.AuthLoginInputToggle-type')
        elem.click()
        elem = driver.find_element(by='id', value='passp-field-login')
        elem.send_keys('snobik57@yandex.ru')
        elem = driver.find_element(by='id', value='passp:sign-in')
        elem.click()
        elem = driver.find_element(by='id', value='passp-field-passwd')
        elem.send_keys(get_password('/home/timur/Python_Project/Netology/python_advanced/tests/token.json'))
        elem = driver.find_element(by='id', value='passp:sign-in')
        elem.click()
        sleep(5)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
