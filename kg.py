def get_urls_govori_tv(soup):
    links = list()
    for link in soup.select('div.col-md-12.search div.search-item > a'):
        links.append(link.get('href'))
    return links, 'govori.tv'


def get_urls_oshpirim_kg(soup):
    links = list()
    for link in soup.select('div.mg-posts-sec-inner div.mg-sec-top-post > h1 > a'):
        links.append(link.get('href'))
    return links, 'oshpirim.kg'


def get_urls_maralfm_kg(soup):
    links = list()
    for link in soup.select('ul.mvp-blog-story-list.left.relative.infinite-content li > a'):
        links.append(link.get('href'))
    return links, 'maralfm.kg'


def get_urls_chyndyk_media_kg(soup):
    links = list()
    for link in soup.select('div.td_block_inner.tdb-block-inner.td-fix-index h3 > a'):
        links.append(link.get('href'))
    return links, 'chyndyk.media'


def get_urls_argument_kg(soup):
    links = list()
    for link in soup.select('div.row.video-section.meta-maxwidth-230 h3 > a'):
        links.append(link.get('href'))
    return links, 'argument.kg'


def get_urls_pk_kg(soup):
    links = list()
    for link in soup.select('#w0 h2 > a')[:10]:
        links.append('https://pk.kg' + link.get('href'))
    return links, 'pk.kg'


def get_urls_mezgilnews_kg(soup):
    links = list()
    for link in soup.select('div.posts-wrap.th-list-posts h3 > a')[:10]:
        links.append(link.get('href'))
    return links, 'mezgilnews.kg'


def get_urls_t_media_kg(soup):
    links = list()
    for link in soup.select('div.cactus-sub-wrap h3 > a')[:10]:
        links.append(link.get('href'))
    return links, 't-media.kg'


def get_urls_ring_kg(soup):
    links = list()
    for link in soup.select('div.penci-archive__list_posts h2> a'):
        links.append(link.get('href'))
    return links, 'ring.kg'


def get_urls_slon_kg(soup):
    links = list()
    for link in soup.select('div.col-lg-8 h3 > a'):
        links.append(link.get('href'))
    return links, 'slon.kg'


def get_urls_barometr_kg(soup):
    links = list()
    for link in soup.select('div.col-sm-12 h4 > a'):
        links.append('https://barometr.kg/' + link.get('href'))
    return links, 'barometr.kg'


def get_urls_nazarnews_org(soup):
    links = list()
    for link in soup.select('div.col-12.col-lg-12 h2 > a'):
        links.append('https://nazarnews.org' + link.get('href'))
    return links, 'nazarnews.org'


def get_urls_jebe_kg(soup):
    links = list()
    for link in soup.select('div.td-ss-main-content h3 > a')[:10]:
        links.append(link.get('href'))
    return links, 'jebe.kg'


def get_urls_koom_press(soup):
    links = list()
    for link in soup.select('div.listing.listing-blog.listing-blog-1.clearfix.columns-1 h2 > a'):
        links.append(link.get('href'))
    return links, 'koom.press'


def get_urls_reporter_kg(soup):
    links = list()
    for link in soup.select('div.blog-posts-list.blog-layout-grid.saxon-blog-col-2 h3 > a'):
        links.append(link.get('href'))
    return links, 'reporter.kg'


def get_urls_elgezit_kg(soup):
    links = list()
    for link in soup.select('div.row.large-columns-1.medium-columns-.small-columns-1 div.col-inner > a'):
        links.append(link.get('href'))
    return links, 'elgezit.kg'
