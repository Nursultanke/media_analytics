def get_urls_24(soup):
    links = list()
    for link in soup.select('div.title > a'):
        links.append('https://24.kg' + link.get('href'))
    return links, '24.kg'


def get_urls_kloop(soup):
    links = list()
    for link in soup.select('h3.entry-title > a'):
        links.append(link.get('href'))
    return links, 'kloop.kg'


def get_urls_kaktus_media(soup):
    links = list()
    for link in soup.select('div.t > a'):
        links.append(link.get('href'))
    return links, 'kaktus.media'


def get_urls_rus_azattyk_org(soup):
    links = list()
    for link in soup.select('span.date--mb + a'):
        links.append('https://rus.azattyk.org/' + link.get('href'))
    return links, 'rus.azattyk.org'


def get_urls_ru_sputnik_kg(soup):
    links = list()
    for link in soup.select('h2.b-plainlist__title > a'):
        links.append('https://ru.sputnik.kg/' + link.get('href'))
    return links, 'ru.sputnik.kg'


def get_urls_ktrk_ru(soup):
    links = list()
    for link in soup.select('div.section.search-news-section a.post-title'):
        links.append(link.get('href'))
    return links, 'ktrk.kg_ru'


def get_urls_kabar_kg(soup):
    links = list()
    for link in soup.select('div.search-context h3 > a'):
        links.append('http://www.kabar.kg' + link.get('href'))
    return links, 'ktrk.kg'


def get_urls_bars_media(soup):
    links = list()
    for link in soup.select('.td-main-content h3 > a'):
        links.append(link.get('href'))
    return links, 'bars.media'


def get_urls_vesti_kg(soup):
    links = list()
    for link in soup.select('.result-title > a'):
        links.append('https://vesti.kg' + link.get('href'))
    return links, 'vesti.kg'


def get_urls_bulak_kg(soup):
    links = list()
    for link in soup.select('.ajax-content h2 > a'):
        links.append(link.get('href'))
    return links, 'bulak.kg'


def get_urls_rezonans_kg(soup):
    links = list()
    for link in soup.select('.td-ss-main-content .entry-title.td-module-title > a'):
        links.append(link.get('href'))
    return links, 'rezonans.kg'


def get_urls_yntymak_ru(soup):
    links = list()
    for link in soup.select('.row.grid-view .post-title.p > a'):
        links.append(link.get('href'))
    return links, 'yntymak.kg/ru'


def get_urls_vb_kg(soup):
    links = list()
    for link in soup.select('ul.topic_list.view_lenta_date > li > div.t > a'):
        links.append(link.get('href'))
    return links, 'vb.kg'


def get_urls_akipress_org(soup):
    links = list()
    for link in soup.select('a.aki-news-link'):
        links.append(link.get('href'))
    return links, 'akipress.org'


def get_urls_elgezit_kg(soup):
    links = list()
    for link in soup.select('div.col-inner > a'):
        links.append(link.get('href'))
    return links, 'elgezit.kg'


def get_urls_media_center_kg(soup):
    links = list()
    for link in soup.select('div.search-result-list.dash h2 > a'):
        links.append('https://media-center.kg' + link.get('href'))
    return links, 'media-center.kg'


def get_urls_reporter_kg(soup):
    links = list()
    for link in soup.select('div.blog-posts-list.blog-layout-grid.saxon-blog-col-2 h3 > a'):
        links.append(link.get('href'))
    return links, 'reporter.kg'


def get_urls_koom_press(soup):
    links = list()
    for link in soup.select('div.listing.listing-blog.listing-blog-1.clearfix.columns-1 h2 > a'):
        links.append(link.get('href'))
    return links, 'koom.press'


def get_urls_tuz_kg(soup):
    links = list()
    for link in soup.select('ul.topic_list.view_lenta_date div.t > a')[:10]:
        links.append(link.get('href'))
    return links, 'tuz.kg'


def get_urls_jebe_kg(soup):
    links = list()
    for link in soup.select('div.td-ss-main-content h3 > a'):
        links.append(link.get('href'))
    return links, 'jebe.kg'


def get_urls_nazar_news_org(soup):
    links = list()
    for link in soup.select('div.col-12.col-lg-12 h2 > a'):
        links.append('https://nazarnews.org' + link.get('href'))
    return links, 'nazarnews.org'


def get_urls_barometr_kg(soup):
    links = list()
    for link in soup.select('div.col-sm-12 h4 > a'):
        links.append('https://barometr.kg/' + link.get('href'))
    return links, 'barometr.kg'


def get_urls_slon_kg(soup):
    links = list()
    for link in soup.select('div.col-lg-8 h3 > a'):
        links.append(link.get('href'))
    return links, 'slon.kg'


def get_urls_economist_kg(soup):
    links = list()
    for link in soup.select('ul.list-unstyled.news_list a'):
        links.append(link.get('href'))
    return links, 'economist.kg'


def get_urls_ring_kg(soup):
    links = list()
    for link in soup.select('div.penci-archive__list_posts h2 > a'):
        links.append(link.get('href'))
    return links, 'ring.kg'


def get_urls_sayasat_kg(soup):
    links = list()
    for link in soup.select('dl.search-results dt > a')[:10]:
        links.append('http://www.sayasat.kg' + link.get('href'))
    return links, 'sayasat.kg'
