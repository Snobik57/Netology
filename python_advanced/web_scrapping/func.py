import bs4
import requests
import regex as re


def find_posts_in_habr(html_text: str, keyword: list, headers=None):
    base_url = 'https://habr.com'
    pattern_ = "|".join([fr'(\s{x}\s)' for x in keyword])
    soup = bs4.BeautifulSoup(html_text, features='html.parser')
    articles = soup.find_all(class_="tm-articles-list__item")

    for article in articles:
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        article_link = base_url + href
        resp = requests.get(article_link, headers=headers).text
        art_soup = bs4.BeautifulSoup(resp, features='html.parser').text
        result = re.search(pattern_, art_soup)
        if result:
            article_title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            article_date = article.find('time').attrs['title']

            print(f"{article_date} - {article_title} - {article_link}")
