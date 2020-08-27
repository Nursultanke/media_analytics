def get_urls_24(soup):
    links = list()
    for link in soup.select('div.title > a:first-child')[:10]:
        links.append('https://24.kg' + link.get('href'))
    return links


def get_urls_kloop(soup):
    links = list()
    for link in soup.select('h3.entry-title > a')[:2]:
        links.append(link.get('href'))
    return links


def get_urls_kaktus_media(soup):
    links = list()
    for link in soup.select('div.t > a')[:10]:
        links.append(link.get('href'))
    return links


def get_urls_rus_azattyk_org(soup):
    links = list()
    for link in soup.select('span.date--mb + a')[:5]:
        links.append('https://rus.azattyk.org' + link.get('href'))
    return links


def get_urls_azattyk_org(soup):
    links = list()
    for link in soup.select('span.date--mb + a')[:5]:
        links.append('https://azattyk.org' + link.get('href'))
    return links


def get_urls_ru_sputnik_kg(soup):
    links = list()
    for link in soup.select('h2.b-plainlist__title > a')[:5]:
        links.append('https://ru.sputnik.kg/' + link.get('href'))
    return links


def get_urls_sputnik_kg(soup):
    links = list()
    for link in soup.select('h2.b-plainlist__title > a')[:5]:
        links.append('https://sputnik.kg/' + link.get('href'))
    return links


def get_urls_ktrk_ru(soup):
    links = list()
    for link in soup.select('div.section-body a.post-title')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_kabar_kg(soup):
    links = list()
    for link in soup.select('div.col-md-8 article.simple-post.simple-big.clearfix h3 > a')[:10]:
        links.append('http://www.kabar.kg' + link.get('href'))
    return links


def get_urls_kg_kabar_kg(soup):
    links = list()
    for link in soup.select('div.search-context h3 > a')[:5]:
        links.append('http://kg.kabar.kg/' + link.get('href'))
    return links


def get_urls_bars_media(soup):
    links = list()
    for link in soup.select('.td-main-content h3 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_vesti_kg(soup):
    links = list()
    for link in soup.select('.result-title > a')[:5]:
        links.append('https://vesti.kg' + link.get('href'))
    return links


def get_urls_bulak_kg(soup):
    links = list()
    for link in soup.select('.ajax-content h2 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_rezonans_kg(soup):
    links = list()
    for link in soup.select('.td-ss-main-content .entry-title.td-module-title > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_yntymak_ru(soup):
    links = list()
    for link in soup.select('.row.grid-view .post-title.p > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_vb_kg(soup):
    links = list()
    for link in soup.select('ul.topic_list.view_lenta_date > li > div.t > a')[:10]:
        links.append(link.get('href'))
    return links


def get_urls_akipress_org(soup):
    links = list()
    for link in soup.select('a.aki-news-link'):
        links.append('http://kg.akipress.org' + link.get('href'))
    return links


def get_urls_elgezit_kg(soup):
    links = list()
    for link in soup.select('div.col-inner > a'):
        links.append(link.get('href'))
    return links


def get_urls_media_center_kg(soup):
    links = list()
    for link in soup.select('div.category-news-list.dash h2 > a')[:5]:
        links.append('https://media-center.kg' + link.get('href'))
    return links


def get_urls_reporter_kg(soup):
    links = list()
    for link in soup.select('div#content h3 > a'):
        links.append(link.get('href'))
    return links


def get_urls_koom_press(soup):
    links = list()
    for link in soup.select('div.listing.listing-blog.listing-blog-1.clearfix.columns-1 h2 > a'):
        links.append(link.get('href'))
    return links


def get_urls_tuz_kg(soup):
    links = list()
    for link in soup.select('ul.topic_list.view_lenta_date div.t > a')[:10]:
        links.append(link.get('href'))
    return links


def get_urls_jebe_kg(soup):
    links = list()
    for link in soup.select('div.td-ss-main-content h3 > a'):
        links.append(link.get('href'))
    return links


def get_urls_nazar_news_org(soup):
    links = list()
    for link in soup.select('div.col-12.col-lg-12 h2 > a')[:5]:
        links.append('https://nazarnews.org' + link.get('href'))
    return links


def get_urls_barometr_kg(soup):
    links = list()
    for link in soup.select('div.col-sm-12 h4 > a'):
        links.append('https://barometr.kg/' + link.get('href'))
    return links


def get_urls_slon_kg(soup):
    links = list()
    for link in soup.select('div.col-lg-8 h3 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_economist_kg(soup):
    links = list()
    for link in soup.select('ul.list-unstyled.news_list li > a'):
        links.append(link.get('href'))
    return links


def get_urls_ring_kg(soup):
    links = list()
    for link in soup.select('div.penci-archive__list_posts h2> a'):
        links.append(link.get('href'))
    return links


def get_urls_sayasat_kg(soup):
    links = list()
    for link in soup.select('div.blog h2[itemprop="name"] > a')[:5]:
        links.append('http://www.sayasat.kg' + link.get('href'))
    return links


def get_urls_govori_tv(soup):
    links = list()
    for link in soup.select('div.col-md-12.search div.search-item > a')[:10]:
        links.append(link.get('href'))
    return links


def get_urls_oshpirim_kg(soup):
    links = list()
    for link in soup.select('div.mg-posts-sec-inner div.mg-sec-top-post > h1 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_maralfm_kg(soup):
    links = list()
    for link in soup.select('ul.mvp-blog-story-list.left.relative.infinite-content li > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_chyndyk_media_kg(soup):
    links = list()
    for link in soup.select('div.td_block_inner.tdb-block-inner.td-fix-index h3 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_argument_kg(soup):
    links = list()
    for link in soup.select('div.row.video-section.meta-maxwidth-230 h3 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_pk_kg(soup):
    links = list()
    for link in soup.select('#w0 h2 > a')[:10]:
        links.append('https://pk.kg' + link.get('href'))
    return links


def get_urls_mezgilnews_kg(soup):
    links = list()
    for link in soup.select('div.posts-wrap.th-list-posts h3 > a')[:5]:
        links.append(link.get('href'))
    return links


def get_urls_t_media_kg(soup):
    links = list()
    for link in soup.select('div.main-content-col div.cactus-sub-wrap h3 > a')[:10]:
        links.append(link.get('href'))
    return links


def get_urls_knews_kg(soup):
    links = list()
    for link in soup.select('div.td-ss-main-content h3.entry-title.td-module-title > a')[:10]:
        links.append(link.get('href'))
    return links


def get_urls_saat_kg(soup):
    links = list()
    for link in soup.select('div.td-ss-main-content h3 > a')[:2]:
        links.append(link.get('href'))
    return links


def get_urls_eldik_media_kg(soup):
    links = list()
    for link in soup.select('div.ui.middle.aligned.selection.list > a')[:2]:
        links.append(link.get('href'))
    return links


def get_urls_kabarlar_kg(soup):
    links = list()
    for link in soup.select('div.ui.relaxed.divided.selection.list > a'):
        links.append(link.get('href'))
    return links


def get_urls_racurs_kg(soup):
    links = list()
    for link in soup.select('div.td_block_inner.tdb-block-inner.td-fix-index h3 > a')[:2]:
        links.append(link.get('href'))
    return links


def get_urls_super_info(soup):
    links = list()
    for link in soup.select('td.content a.item_title')[:2]:
        links.append('https://www.super.kg/' + link.get('href'))
    return links