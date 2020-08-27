import article_pars as art
import get_url as get_url

keyword_ru = 'выборы'
keyword_kg = 'шайлоо'

urls = {
    # '24.kg': {
    #     'ru_link': 'https://24.kg/poisk_po_sajtu/?SearchForm%5Btext%5D=' + keyword_ru,
    #     'kg_link': 'https://24.kg/poisk_po_sajtu/?SearchForm%5Btext%5D=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_24,
    #     'pars_article': art.get_article_24,
    # },
    # 'kloop.kg': {
    #     'ru_link': 'https://kloop.kg/?s=' + keyword_ru,
    #     'kg_link': 'https://ky.kloop.asia/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_kloop,
    #     'pars_article': art.get_article_kloop,
    # },
    # 'kaktus.media': {
    #     'ru_link': 'https://kaktus.media/?search=' + keyword_ru,
    #     'pars_link_list': get_url.get_urls_kaktus_media,
    #     'pars_article': art.get_article_kakatus_media,
    # },
    # 'rus.azattyk.org': {
    #     'ru_link': 'https://rus.azattyk.org/s?k=' + keyword_ru + '&tab=news&pi=1&r=week&pp=20',
    #     'pars_link_list': get_url.get_urls_rus_azattyk_org,
    #     'pars_article': art.get_article_azattyk_org,
    # },
    # 'azattyk.org': {
    #     'kg_link': 'https://www.azattyk.org/s?k=' + keyword_kg + '&tab=all&pi=1&r=any&pp=10',
    #     'pars_link_list': get_url.get_urls_azattyk_org,
    #     'pars_article': art.get_article_azattyk_org,
    # },
    # 'ru.sputnik.kg': {
    #     'ru_link': 'https://ru.sputnik.kg/services/search/getmore/?' + keyword_ru + '=' + keyword_ru + '&search_area=all&query%5B%5D=' + keyword_ru + '&limit=20&offset=0&sort=date&interval=period',
    #     'pars_link_list': get_url.get_urls_ru_sputnik_kg,
    #     'pars_article': art.get_article_sputnik,
    # },
    # 'sputnik.kg': {
    #     'kg_link': 'https://sputnik.kg/services/search/getmore/?' + keyword_kg + '=' + keyword_kg + '&search_area=all&query%5B%5D=' + keyword_kg + '&limit=20&offset=0&sort=date&interval=period' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_sputnik_kg,
    #     'pars_article': art.get_article_sputnik,
    # },
    # 'ktrk.kg': {
    #     'ru_link': 'http://www.ktrk.kg/ru/category/29',
    #     'kg_link': 'http://www.ktrk.kg/category/29',
    #     'pars_link_list': get_url.get_urls_ktrk_ru,
    #     'pars_article': art.get_article_ktrk,
    # },
    # 'kabar.kg': {
    #     'ru_link': 'http://www.kabar.kg/cat/vybory-2020/',
    #     'pars_link_list': get_url.get_urls_kabar_kg,
    #     'pars_article': art.get_article_kabar,
    # },
    # 'kg.kabar.kg': {
    #     'kg_link': 'http://kg.kabar.kg/search/?q=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_kg_kabar_kg,
    #     'pars_article': art.get_article_kabar,
    # },    # 'kg.kabar.kg': {
    #     'kg_link': 'http://kg.kabar.kg/search/?q=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_kg_kabar_kg,
    #     'pars_article': art.get_article_kabar,
    # },
    # 'bars.media': {
    #     'ru_link': 'https://bars.media/?s=' + keyword_ru,
    #     'kg_link': 'https://bars.media/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_bars_media,
    #     'pars_article': art.get_article_bars_media,
    # },
    # 'vesti.kg': {
    #     'ru_link': 'https://vesti.kg/component/search/?searchword=' + keyword_ru + '&ordering=newest&searchphrase=exact&limit=20',
    #     'kg_link': 'https://vesti.kg/kg/component/search/?searchword=' + keyword_kg + '&searchphrase=all&Itemid=9999',
    #     'pars_link_list': get_url.get_urls_vesti_kg,
    #     'pars_article': art.get_article_vesti,
    # },
    # 'bulak.kg': {
    #     'ru_link': 'https://bulak.kg/article/search?q=' + keyword_ru,
    #     'kg_link': 'https://bulak.kg/kyr/article/search?q=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_bulak_kg,
    #     'pars_article': art.get_article_bulak,
    # },
    # 'rezonans.kg': {
    #     'ru_link': 'https://rezonans.kg/?s=' + keyword_ru,
    #     'pars_link_list': get_url.get_urls_rezonans_kg,
    #     'pars_article': art.get_article_rezonans,
    # },
    # 'yntymak.kg': {
    #     'ru_link': 'http://yntymak.kg/ru/?s=' + keyword_ru,
    #     'kg_link': 'http://yntymak.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_yntymak_ru,
    #     'pars_article': art.get_article_yntymak,
    # },
    # 'vb.kg': {
    #     'ru_link': 'https://www.vb.kg/?search=' + keyword_ru,
    #     'kg_link': 'https://www.vb.kg/?search=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_vb_kg,
    #     'pars_article': art.get_article_vb,
    # },
    # 'akipress.org': {
    #     'ru_link': 'http://kg.akipress.org/find/?find=%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D1%8B&place=default-form&s=0&p=1&d=1&tools=1',
    #     'pars_link_list': get_url.get_urls_akipress_org,
    #     'pars_article': art.get_article_akipress,
    # },
    # 'elgezit.kg': {
    #     'ru_link': 'https://elgezit.kg/?s=' + keyword_ru,
    #     'kg_link': 'https://elgezit.kg/ky/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_elgezit_kg,
    #     'pars_article': art.get_article_elgezit,
    # },
    # 'media-center.kg': {
    #     'ru_link': 'https://media-center.kg/ru/category/voting-2020',
    #     'kg_link': 'https://media-center.kg/kg/category/voting-2020',
    #     'pars_link_list': get_url.get_urls_media_center_kg,
    #     'pars_article': art.get_article_media_center,
    # },
    # 'reporter.kg': {
    #     'ru_link': 'https://ru.reporter.kg/category/vybory-2020/',
    #     'kg_link': 'https://reporter.kg/category/shajloo-2020/',
    #     'pars_link_list': get_url.get_urls_reporter_kg,
    #     'pars_article': art.get_article_reporter,
    # },
    # 'koom.press': {
    #     'ru_link': 'https://koom.press/ru/?s=' + keyword_ru,
    #     'kg_link': 'https://koom.press/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_koom_press,
    #     'pars_article': art.get_article_koom_press,
    # },
    # 'tuz.kg': {
    #     'ru_link': 'https://www.tuz.kg/?search=' + keyword_ru,
    #     'pars_link_list': get_url.get_urls_tuz_kg,
    #     'pars_article': art.get_article_tuz,
    # },
    # 'jebe.kg': {
    #     'ru_link': 'http://jebe.kg/?s=' + keyword_ru,
    #     'kg_link': 'http://jebe.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_jebe_kg,
    #     'pars_article': art.get_article_jebe,
    # },
    # 'nazarnews.org': {
    #     'ru_link': 'https://nazarnews.org/search_post?search_query=' + keyword_ru,
    #     'kg_link': 'https://nazarnews.org/search_post?search_query=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_nazar_news_org,
    #     'pars_article': art.get_article_nazarnews,
    # },
    # 'barometr.kg': {
    #     'ru_link': 'https://barometr.kg/search?q=' + keyword_ru,
    #     'kg_link': 'https://barometr.kg/search?q=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_barometr_kg,
    #     'pars_article': art.get_article_barometr,
    # },
    # 'slon.kg': {
    #     'ru_link': 'http://slon.kg/?s=' + keyword_ru,
    #     'kg_link': 'http://slon.kg/kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_slon_kg,
    #     'pars_article': art.get_article_slon,
    # },
    # 'economist.kg': {
    #     'ru_link': 'https://economist.kg/?s=' + keyword_ru,
    #     'pars_link_list': get_url.get_urls_economist_kg,
    #     'pars_article': art.get_article_economist,            #chalishmiyor
    # },
    # 'ring.kg': {
    #     'ru_link': 'http://ring.kg/?lang=ru&s=' + keyword_ru,
    #     'kg_link': 'http://ring.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_ring_kg,
    #     'pars_article': art.get_article_ring,
    # },
    # 'sayasat.kg': {
    #     'ru_link': 'http://www.sayasat.kg/elections-2020.html',
    #     'kg_link': 'http://www.sayasat.kg/kg/shilolo-2020.html',
    #     'pars_link_list': get_url.get_urls_sayasat_kg,
    #     'pars_article': art.get_article_sayasat,
    # },
    # 'govori.tv': {
    #     'ru_link': 'https://govori.tv/?s=' + keyword_ru + '&cat=2673&submit=',
    #     'kg_link': 'https://govori.tv/?s=' + keyword_kg + '&cat=-1&submit=',
    #     'pars_link_list': get_url.get_urls_govori_tv,
    #     'pars_article': art.get_article_govori,
    # },
    # 'oshpirim.kg': {
    #     'kg_link': 'https://oshpirim.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_oshpirim_kg,
    #     'pars_article': art.get_article_oshpirim,
    # },
    # 'maralfm.kg': {
    #     'kg_link': 'https://maralfm.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_maralfm_kg,
    #     'pars_article': art.get_article_maralfm,
    # },
    # 'chyndyk.media': {
    #     'kg_link': 'https://chyndyk.media/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_chyndyk_media_kg,
    #     'pars_article': art.get_article_chyndyk_media,
    # },
    # 'argument.kg': {
    #     'kg_link': 'https://argument.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_argument_kg,
    #     'pars_article': art.get_article_argument,
    # },
    # 'pk.kg': {
    #     'kg_link': 'https://pk.kg/news/search?search=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_pk_kg,
    #     'pars_article': art.get_article_pk,
    # },
    # 'mezgilnews.kg': {
    #     'kg_link': 'https://mezgilnews.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_mezgilnews_kg,
    #     'pars_article': art.get_article_mezgilnews,
    # },
    # 't-media.kg': {
    #     'kg_link': 'http://t-media.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_t_media_kg,
    #     'pars_article': art.get_article_t_media,
    # },
    # 'knews.kg': {
    #     'ru_link': 'https://knews.kg/vlast/vybory',
    #     'pars_link_list': get_url.get_urls_knews_kg,
    #     'pars_article': art.get_article_knews,
    # },
    # 'saat.kg': {
    #     'kg_link': 'https://saat.kg/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_saat_kg,
    #     'pars_article': art.get_article_saat,
    # },
    # 'eldik.media': {
    #     'ru_link': 'https://eldik.media/ru/?s=' + keyword_ru,
    #     'kg_link': 'https://eldik.media/?s=' + keyword_kg,
    #     'pars_link_list': get_url.get_urls_saat_kg,
    #     'pars_article': art.get_article_eldik_media,
    # },
    # 'kabarlar.org': {
    #     'ru_link': 'https://kabarlar.org/election2020',
    #     'pars_link_list': get_url.get_urls_kabarlar_kg,
    #     'pars_article': art.get_article_kabarlar,
    # },
    'racurs.kg': {
        'kg_link': 'https://racurs.kg/?s=' + keyword_kg,
        'pars_link_list': get_url.get_urls_racurs_kg,
        'pars_article': art.get_article_racurs,
    },
    # 'super.info': {
    #     'kg_link': 'https://www.super.kg/search/?where_to_search=article&search_term=' + keyword_kg + '&x=0&y=0',
    #     'pars_link_list': get_url.get_urls_super_info,
    #     'pars_article': art.get_article_super_info,
    # },
}

stop_words = (
"фото", "в", "c", "а", "алло", "без", "белый", "близко", "более", "больше", "большой", "будем", "будет", "будете",
"будешь", "будто", "буду", "будут", "будь", "бы", "бывает", "бывь", "был", "была", "были", "было", "быть", "в",
"важная", "важное", "важные", "важный", "вам", "вами", "вас", "ваш", "ваша", "ваше", "ваши", "вверх", "вдали", "вдруг",
"ведь", "везде", "вернуться", "весь", "вечер", "взгляд", "взять", "вид", "видел", "видеть", "вместе", "вне", "вниз",
"внизу", "во", "вода", "война", "вокруг", "вон", "вообще", "вопрос", "восемнадцатый", "восемнадцать", "восемь",
"восьмой", "вот", "впрочем", "времени", "время", "все", "все еще", "всегда", "всего", "всем", "всеми", "всему", "всех",
"всею", "всю", "всюду", "вся", "всё", "второй", "вы", "выйти", "г", "где", "главный", "глаз", "говорил", "говорит",
"говорить", "год", "года", "году", "голова", "голос", "город", "да", "давать", "давно", "даже", "далекий", "далеко",
"дальше", "даром", "дать", "два", "двадцатый", "двадцать", "две", "двенадцатый", "двенадцать", "дверь", "двух",
"девятнадцатый", "девятнадцать", "девятый", "девять", "действительно", "дел", "делал", "делать", "делаю", "дело",
"день", "деньги", "десятый", "десять", "для", "до", "довольно", "долго", "должен", "должно", "должный", "дом", "дорога",
"друг", "другая", "другие", "других", "друго", "другое", "другой", "думать", "душа", "е", "его", "ее", "ей", "ему",
"если", "есть", "еще", "ещё", "ею", "её", "ж", "ждать", "же", "жена", "женщина", "жизнь", "жить", "за", "занят",
"занята", "занято", "заняты", "затем", "зато", "зачем", "здесь", "земля", "знать", "значит", "значить", "и", "иди",
"идти", "из", "или", "им", "имеет", "имел", "именно", "иметь", "ими", "имя", "иногда", "их", "к", "каждая", "каждое",
"каждые", "каждый", "кажется", "казаться", "как", "какая", "какой", "кем", "книга", "когда", "кого", "ком", "комната",
"кому", "конец", "конечно", "которая", "которого", "которой", "которые", "который", "которых", "кроме", "кругом", "кто",
"куда", "лежать", "лет", "ли", "лицо", "лишь", "лучше", "любить", "люди", "м", "маленький", "мало", "мать", "машина",
"между", "меля", "менее", "меньше", "меня", "место", "миллионов", "мимо", "минута", "мир", "мира", "мне", "много",
"многочисленная", "многочисленное", "многочисленные", "многочисленный", "мной", "мною", "мог", "могу", "могут", "мож",
"может", "может быть", "можно", "можхо", "мои", "мой", "мор", "москва", "мочь", "моя", "моё", "мы", "на", "наверху",
"над", "надо", "назад", "наиболее", "найти", "наконец", "нам", "нами", "народ", "нас", "начала", "начать", "наш",
"наша", "наше", "наши", "не", "него", "недавно", "недалеко", "нее", "ней", "некоторый", "нельзя", "нем", "немного",
"нему", "непрерывно", "нередко", "несколько", "нет", "нею", "неё", "ни", "нибудь", "ниже", "низко", "никакой",
"никогда", "никто", "никуда", "ним", "ними", "них", "ничего", "ничто", "но", "новый", "нога", "ночь", "ну", "нужно",
"нужный", "нх", "о", "об", "оба", "обычно", "один", "одиннадцатый", "одиннадцать", "однажды", "однако", "одного",
"одной", "оказаться", "окно", "около", "он", "она", "они", "оно", "опять", "особенно", "остаться", "от", "ответить",
"отец", "откуда", "отовсюду", "отсюда", "очень", "первый", "перед", "писать", "плечо", "по", "под", "подойди",
"подумать", "пожалуйста", "позже", "пойти", "пока", "пол", "получить", "помнить", "понимать", "понять", "пор", "пора",
"после", "последний", "посмотреть", "посреди", "потом", "потому", "почему", "почти", "правда", "прекрасно", "при",
"про", "просто", "против", "процентов", "путь", "пятнадцатый", "пятнадцать", "пятый", "пять", "работа", "работать",
"раз", "разве", "рано", "раньше", "ребенок", "решить", "россия", "рука", "русский", "ряд", "рядом", "с", "с кем", "сам",
"сама", "сами", "самим", "самими", "самих", "само", "самого", "самой", "самом", "самому", "саму", "самый", "свет",
"свое", "своего", "своей", "свои", "своих", "свой", "свою", "сделать", "сеаой", "себе", "себя", "сегодня", "седьмой",
"сейчас", "семнадцатый", "семнадцать", "семь", "сидеть", "сила", "сих", "сказал", "сказала", "сказать", "сколько",
"слишком", "слово", "случай", "смотреть", "сначала", "снова", "со", "собой", "собою", "советский", "совсем", "спасибо",
"спросить", "сразу", "стал", "старый", "стать", "стол", "сторона", "стоять", "страна", "суть", "считать", "т", "та",
"так", "такая", "также", "таки", "такие", "такое", "такой", "там", "твои", "твой", "твоя", "твоё", "те", "тебе", "тебя",
"тем", "теми", "теперь", "тех", "то", "тобой", "тобою", "товарищ", "тогда", "того", "тоже", "только", "том", "тому",
"тот", "тою", "третий", "три", "тринадцатый", "тринадцать", "ту", "туда", "тут", "ты", "тысяч", "у", "увидеть", "уж",
"уже", "улица", "уметь", "утро", "хороший", "хорошо", "хотел бы", "хотеть", "хоть", "хотя", "хочешь", "час", "часто",
"часть", "чаще", "чего", "человек", "чем", "чему", "через", "четвертый", "четыре", "четырнадцатый", "четырнадцать",
"что", "чтоб", "чтобы", "чуть", "шестнадцатый", "шестнадцать", "шестой", "шесть", "эта", "эти", "этим", "этими", "этих",
"это", "этого", "этой", "этом", "этому", "этот", "эту", "я", "являюсь")
