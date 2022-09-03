import requests
from user_agent import generate_navigator
from func import find_posts_in_habr

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = 'https://habr.com'
url = base_url + "/ru/all/"

HEADERS = generate_navigator()

response = requests.get(url, headers=HEADERS)
text = response.text

if __name__ == '__main__':
    find_posts_in_habr(text, KEYWORDS, headers=HEADERS)
