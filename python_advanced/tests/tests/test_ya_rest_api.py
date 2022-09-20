import pytest
import requests
from Netology.python_advanced.tests.ya_rest_api import UsersYD


@pytest.fixture()
def teardown():
    print('START')
    yield
    url = UsersYD().url
    headers = UsersYD().headers
    params = {
        'path': 'new_folder',
        'permanently': 'true'
    }
    requests.delete(url, params=params, headers=headers)


def test_correct_folder_creation(teardown):
    resp = UsersYD().create_folder('new_folder')
    assert resp.status_code in [200, 201]
    return resp


def test_folder_presence(teardown):
    resp = UsersYD().create_folder('new_folder')
    assert 'href' in resp.json().keys()


@pytest.mark.xfail()
def test_fail_folder_creation(teardown):
    resp = UsersYD().create_folder('new_folder')
    assert resp.status_code in [400, 401, 403, 404, 406, 409, 413, 423, 429, 503, 507]








