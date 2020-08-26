def get_article_24(soup):
    result = {}
    try:
        result['article'] = soup.select('div[itemprop="articleBody"]')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('.newsTitle')[0].getText().strip().replace('\xa0', ' ').replace('\n', ' ')
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('span[itemprop="datePublished"]')[0].get('content')[:-1].strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span[itemprop="name"].text-nowrap')[0].getText().strip()
    except IndexError:
        pass
    return result


def get_article_kloop(soup):
    result = {}
    try:
        result['article'] = soup.select('div[data-ui-id="post"]')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('h1')[0].getText().strip().replace('\xa0', ' ').replace('\n', ' ')
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        result['author'] = soup.find('div', class_='td-post-author-name').find('a').getText().strip().replace('\xa0', ' ')
    except AttributeError:
        pass
    return result


def get_article_kakatus_media(soup):
    result = {}
    try:
        result['article'] = soup.select('div[itemprop="articleBody"]')[0].getText(separator=u' ').strip().replace(
            '\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('span', attrs={"itemprop": "headline"}).getText().strip().replace('\xa0',
                                                                                                      ' ').replace('\n',
                                                                                                                   ' '),
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    return result


def get_article_azattyk_org(soup):
    result = {}
    article = ''
    article_items = soup.find('div', class_='wsw').find_all('p')
    for item in article_items:
        article = article + item.getText()
    try:
        result['article'] = article
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1', class_='title pg-title').getText().strip().replace('\xa0', ' ').replace('\n',
                                                                                                                  ' ')
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        result['author'] = soup.select('a.links__item-link')[0].getText().strip()
    except IndexError:
        pass
    return result


def get_article_sputnik(soup):
    result = {}
    try:
        result['article'] = soup.select('div.b-article__text')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('h1')[0].getText().strip().replace('\xa0', ' ').replace('\n', ' ')
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    return result

# sputnik


def get_article_ktrk(soup):
    result = {}
    article = ''
    article_items = soup.find('section', class_='clearfix').find_all('p')
    for item in article_items:
        article = article + item.getText()
    try:
        result['article'] = article.strip().replace('\xa0', ' ')
    except AttributeError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('p', class_='main-news-title').getText().strip().replace('\xa0', ' ').replace('\n',
                                                                                                                  ' ')
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('span', class_='main-news-date').getText().strip(),
    except AttributeError:
        pass
    return result


def get_article_kabar(soup):
    result = {}
    article = ''
    article_items = soup.find('div', class_='post-content clearfix').find_all('p')
    for item in article_items:
        article = article + item.getText()
    try:
        result['article'] = article.strip().replace('\xa0', ' ')
    except AttributeError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('h1')[0].getText().strip().replace('\xa0', ' ').replace('\n', ' ').strip(),
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('span', class_='article-date').getText().strip(),
    except IndexError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_bars_media(soup):
    result = {}
    try:
        result['article'] = soup.select('div.td-post-content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('h1.entry-title')[0].getText().strip().replace('\xa0', ' ').replace('\n', ' '),
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime'),
    except AttributeError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_vesti(soup):
    result = {}
    try:
        result['article'] = soup.select('div.itemFullText')[0].getText(separator=u' ').strip().replace('\xa0', ' '),
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip(),
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime'),
    except IndexError:
        pass
    try:
        result['author'] = 'no author'
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_bulak(soup):
    result = {}
    try:
        result['article'] = soup.select('div.text-article.mce-content-body')[0].getText(separator=u' ').strip().replace(
            '\xa0', ' '),
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip(),
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime'),
    except IndexError:
        pass
    try:
        result['author'] = 'no author'
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_rezonans(soup):
    result = {}
    try:
        result['article'] = soup.select('div.td-post-content.td-pb-padding-side')[0].getText(
            separator=u' ').strip().replace('\xa0', ' ').strip(),
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip(),
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime'),
    except IndexError:
        pass
    try:
        result['author'] = 'no author'
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_yntymak(soup):
    result = {}
    try:
        result['article'] = soup.select('div.post-enter.margin-bottom-30 p')[0].getText(separator=u' ').strip().replace(
            '\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('div', class_='post-thumb-overlay').find('h2').getText().replace('\xa0',
                                                                                                     ' ').replace('\n',
                                                                                                                  ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('li', class_='s-date post-date-li').getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.find('a', class_='name').getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_vb(soup):
    result = {}
    try:
        result['article'] = soup.select('div.topic-text')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.topic-authors')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_elgezit(soup):
    result = {}
    try:
        result['article'] = soup.select('div.entry-content.single-page')[0].getText(separator=u' ').strip().replace(
            '\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1', class_='entry-title').getText().replace('\xa0', ' ').replace('\n',
                                                                                                       ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('i', class_='far fa-calendar-alt').getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.topic-authors')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_media_center(soup):
    result = {}
    try:
        result['article'] = soup.select('div.text')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1', class_='news-title').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('div', class_='news-item__date grey').getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('div.news-item__author grey > a')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_reporter(soup):
    result = {}
    try:
        result['article'] = soup.select('div.entry-content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1', class_='post-title').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('div', class_='post-date post-time').find('p').getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('div.news-item__author grey > a')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_koom_press(soup):
    result = {}
    try:
        result['article'] = soup.select('div.entry-content.clearfix.single-post-content')[0].getText(
            separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('span', class_='post-title').getText().replace('\xa0', ' ').replace('\n',
                                                                                                        ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except IndexError:
        pass
    try:
        result['author'] = soup.find('span', class_='post-author-name').getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_tuz(soup):
    result = {}
    try:
        result['article'] = soup.select('div.topic-text')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.post-author-name')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_jebe(soup):
    result = {}
    try:
        result['article'] = soup.select('div.td-post-content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.post-author-name')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_nazarnews(soup):
    result = {}
    try:
        result['article'] = soup.select('#post_desc')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h5', class_='font-weight-bold').getText().replace('\xa0', ' ').replace('\n',
                                                                                                            ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('span', class_='entry-date').getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.post-author-name')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_barometr(soup):
    result = {}
    try:
        result['article'] = soup.select('div.content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('span', class_='aticle_published').getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.aticle_author')[0].getText().strip()
    except IndexError:
        result['author'] = 'no author'
    return result


def get_article_slon(soup):
    result = {}
    try:
        result['article'] = soup.select('div.entry-content.clearfix')[0].getText(separator=u' ').strip().replace('\xa0',
                                                                                                                 ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h2', class_='post-title lg').getText().replace('\xa0', ' ').replace('\n',
                                                                                                         ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('ul.post-meta-info > li')[0].getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('span.aticle_author')[0].getText().strip()
    except IndexError:
        pass
    return result


def get_article_economist(soup):
    result = {}
    try:
        result['article'] = soup.select('div.a_desc')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('span', class_='title_article').find('h2').getText().replace('\xa0', ' ').replace(
            '\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('span.date_article')[0].getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.find('div', class_='cats').getText().strip()
    except AttributeError:
        pass
    return result


def get_article_ring(soup):
    result = {}
    try:
        result['article'] = soup.select('div.penci-entry-content.entry-content')[0].getText(
            separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_sayasat(soup):
    result = {}
    try:
        result['article'] = soup.select('div[itemprop="articleBody"]')[0].getText(separator=u' ').strip().replace(
            '\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('h2[itemprop="headline1"]')[0].getText().replace('\xa0', ' ').replace('\n',
                                                                                                            ' ').strip()
    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_govori(soup):
    result = {}
    try:
        article = ''
        for i in soup.find('div', class_='col-md-9 left').findAll('div', class_='row')[1:]:
            i.decompose()
        article_items = soup.find('div', class_='col-md-9 left').findAll('p').strip().replace('\xa0', ' ')
        for item in article_items:
            article = article + item.getText()
        result['article'] = article
    except AttributeError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('div', class_='time').getText().strip()
    except AttributeError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_oshpirim(soup):
    result = {}
    try:
        result['article'] = soup.select('article.small.single')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1', class_='title single').find('a').getText().replace('\xa0', ' ').replace('\n',
                                                                                                                  ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('div.media-body > span')[0].getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.find('h4', class_='media-heading').find('a').getText().strip()
    except AttributeError:
        pass
    return result


def get_article_maralfm(soup):
    result = {}
    try:
        result['article'] = soup.find('div', class_='theiaPostSlider_preloadedSlide').getText().strip().replace('\xa0',
                                                                                                                ' ')
    except AttributeError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('div.custom-breadcrumb')[0].getText().split('|')[1].strip()
    except IndexError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_chyndyk_media(soup):
    result = {}
    try:
        result['article'] = soup.select('div.td-post-content.tagdiv-type')[0].getText(separator=u' ').strip().replace(  '\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        result['author'] = soup.find('div', class_='td-post-author-name').find('a').getText().strip()
    except AttributeError:
        pass
    return result


def get_article_argument(soup):
    result = {}
    try:
        result['article'] = soup.select('div.post-entry')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('div', class_='post-header').find('h2').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('span.post-meta')[0].getText().split('/')[1].strip()
    except IndexError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_pk(soup):
    result = {}
    try:
        result['article'] = soup.select('div.SimpleBlock-p')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('time.Timestamp-root')[0].getText().strip()
    except IndexError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_mezgilnews(soup):
    result = {}
    try:
        result['article'] = soup.select('div.entry-content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result


def get_article_t_media(soup):
    result = {}
    try:
        result['article'] = soup.select('div.body-content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()
    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        result['author'] = soup.select('a.vcard.author.cactus-info.font-size-1 > span.fn')[0].getText().strip()
    except IndexError:
        pass
    return result


def get_article_knews(soup):
    result = {}
    try:
        result['article'] = soup.select('div.intro.intro--bold')[0].getText(separator=u' ').strip().replace('\xa0',
                                                                                                            ' ') + \
                            soup.select('div#article-content')[0].getText(separator=u' ').strip().replace('\xa0', ' ')
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()

    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('div.entry-date.updated.td-module-date')[0].getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('a.author.url.fn')[0].getText().strip()
    except IndexError:
        pass
    return result


def get_article_saat(soup):
    result = {}
    try:
        result['article'] = soup.select('div.td-post-content')[0].getText(separator=u' ').strip().replace('\xa0',
                                                                                                          ' ').strip()
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()

    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('div.entry-date.updated.td-module-date')[0].getText().strip()
    except IndexError:
        pass
    try:
        result['author'] = soup.select('a.author.url.fn')[0].getText().strip()
    except IndexError:
        pass
    return result


def get_article_eldik_media(soup):
    result = {}
    try:
        result['article'] = soup.select('div.td-post-content')[0].getText(separator=u' ').strip().replace('\xa0',
                                                                                                          ' ').strip()
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.find('h1').getText().replace('\xa0', ' ').replace('\n', ' ').strip()

    except AttributeError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.find('time').get('datetime')
    except AttributeError:
        pass
    try:
        result['author'] = soup.find('div', class_='td-post-author-name').getText().strip()
    except AttributeError:
        pass
    return result


def get_article_kabarlar(soup):
    result = {}
    try:
        result['article'] = soup.select('article#fullstory')[0].getText(separator=u' ').strip().replace('\xa0',
                                                                                                        ' ').strip()
    except IndexError:
        result['article'] = 'no article'
    try:
        result['title'] = soup.select('h1')[0].getText().replace('\xa0', ' ').replace('\n', ' ').strip()

    except IndexError:
        result['title'] = 'no title'
    try:
        result['date'] = soup.select('div#meta')[2].getText().strip()
    except IndexError:
        pass
    try:
        pass
    except IndexError:
        pass
    return result
