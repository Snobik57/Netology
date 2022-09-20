from selenium import webdriver
import json
from time import sleep


def get_password(path_to_file: str) -> str:
    with open(path_to_file) as file:
        password = json.load(file)['password']
    return password


def get_user_name(email: str) -> list:
    user_name = []
    driver = webdriver.Firefox()
    driver.get('https://passport.yandex.ru/auth/')
    assert "Авторизация" in driver.title

    elem = driver.find_element(by='css selector', value='div.AuthLoginInputToggle-type')
    elem.click()
    elem = driver.find_element(by='id', value='passp-field-login')
    elem.send_keys(email)
    elem = driver.find_element(by='id', value='passp:sign-in')
    elem.click()
    elem = driver.find_element(by='id', value='passp-field-passwd')
    elem.send_keys(get_password('/home/timur/Python_Project/Netology/python_advanced/tests/token.json'))
    elem = driver.find_element(by='id', value='passp:sign-in')
    elem.click()
    sleep(5)
    elem_first = driver.find_element(by='css selector', value='div.personal-info__first')
    user_name.append(elem_first.text)
    elem_last = driver.find_element(by='css selector', value='div.personal-info__last')
    user_name.append(elem_last.text)
    driver.close()

    return user_name


if __name__ == '__main__':
    print(get_user_name('snobik57@yandex.ru'))
