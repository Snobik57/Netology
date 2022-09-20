import requests
import os
import json

class UsersYD:

    def __init__(self):
        with open('/home/timur/Python_Project/Netology/python_advanced/tests/token.json') as file:
            token = json.load(file)['token']
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {
            'Authorization': f'OAuth {self.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.dir_href = None

    def create_folder(self, name_dir: str):
        """
        Метод создает папку на Яндекс Диске пользователя
        :param name_dir: название папки
        :return: None
        """
        params = {
            'path': f'/{name_dir}/'
        }
        resp = requests.put(self.url, headers=self.headers, params=params)
        return resp


if __name__ == '__main__':
    user = UsersYD()
    print(user.create_folder('new_folder_python').json())

