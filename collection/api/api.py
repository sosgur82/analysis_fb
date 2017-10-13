from urllib.parse import urlencode
from .json_request import json_request

ACCESS_TOKEN = '%s|%s' % ('1428253630556936', 'ba8f09769d565fc8646398885bdb20ae')
BASE_URL_FB_API = 'https://graph.facebook.com/v2.8'
LIMIT_REQUEST = 50


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    return '%s/%s/?%s' % (base, node, urlencode(params))


def fb_name_to_id(pagename):
    url = fb_gen_url(
        node=pagename,
        access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    return json_result.get('id')


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields='id,message,link,name,type,shares,\
created_time,reactions.limit(0).summary(true),\
comments.limit(0).summary(true)',
        since=since,
        until=until,
        limit=LIMIT_REQUEST,
        access_token=ACCESS_TOKEN)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield json_result.get('data')

