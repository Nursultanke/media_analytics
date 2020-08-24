from bs4 import BeautifulSoup
import requests

# import pars_module.source_links as variables
# import pars_module.article_analisys as analisys

import source_links as variables

# import os
# import django
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'parser_with_django.settings'
# django.setup()

# from parser_app.models import *


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    return r.text


# def save_db(site_name, site_links, articles_links):
#     new_article = NewArticles()
#     new_article.site_name = site_name
#     new_article.site_link = site_links
#     new_article.new_article_links = articles_links
#     new_article.save()


def check_last_news(articles_links, site, site_name, lang_type):
    for articles_link in articles_links:
        # if exists:
        #     continue
        soup = BeautifulSoup(get_html(articles_link), 'html.parser')
        article_data = site['pars_article'](soup)
        print('Article pars successfully from ' + site_name)
        print(repr(article_data['article']))
        print(article_data)
        # analisys_result = analisys.article_analisys(article_data['article'])
        # TO DO: save to db


def main():
    urls = variables.urls

    for site_name in urls:
        site = urls[site_name]
        if 'ru_link' in site:
            soup = BeautifulSoup(get_html(site['ru_link']), 'html.parser')
            # print(soup)
            print('Html get successfully from ' + site_name)
            articles_links = site['pars_link_list'](soup)
            print('ru', len(articles_links), articles_links)
            print('Articles links pars successfully from ' + site_name)
            check_last_news(articles_links, site, site_name, 'ru')
        if 'kg_link' in site:
            soup = BeautifulSoup(get_html(site['kg_link']), 'html.parser')
            # print(soup)
            print('Html get successfully from ' + site_name)
            articles_links = site['pars_link_list'](soup)
            print('kg', len(articles_links), articles_links)
            print('Articles links pars successfully from ' + site_name)
            check_last_news(articles_links, site, site_name, 'kg')


if __name__ == '__main__':
    main()
