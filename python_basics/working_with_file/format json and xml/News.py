import xml.etree.ElementTree as ET
import json
import collections
from pprint import pprint


def read_json(file_path, max_len_word=6, top_words=10):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        pprint(counter_words.most_common(top_words))


def read_xml(file_path, max_len_word=6, top_words=10):
    with open(file_path, encoding='utf-8') as news_file:
        news = ET.parse(news_file)
        root = news.getroot()
        items_list = root.findall('channel/item')
        description_words = []
        for item in items_list:
            description_txt = [word for word in item[2].text.split(' ') if len(word) > max_len_word]
            description_words.extend(description_txt)
            counter_words = collections.Counter(description_words)
        pprint(counter_words.most_common(top_words))


if __name__ == '__main__':
    read_xml('newsafr.xml')


