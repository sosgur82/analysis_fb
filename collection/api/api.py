from urllib.parse import urlencode
from .json_request import *

ACCESS_TOKEN = '%s|%s' %('1795668674069712','c70756c28d2a49df476cd334dc357892')
BASE_URL_FB_API = 'https://graph.facebook.com/v2.10'
LIMIT_REQUEST=50

def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    return '%s/%s/?%s' % (base, node, urlencode(params))

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    #print(json_result)
    return json_result.get('id')

def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields = 'id,message,link,name,type,shares,\
                  created_time,reactions.limit(0).summary(true),\
                  comments.limit(0).summary(true)',
        since = since,
        until=until,
        limit=LIMIT_REQUEST,
        access_token=ACCESS_TOKEN)
    # print(url)

   # 무한루프를 이용한 다음 자료 얻어오기
    while True:
        json_result = json_request(url=url)

        # 포스트 게시글 20개씩 가져오기
        posts = json_result.get('data')
        paging = json_result.get('paging')

        yield posts

        # next url값 얻어오기
        url =  paging.get('next')

        # next 값이 없을경우 종료해준다.
        if url is None:
            break
    # print(json_result.get('data'))
    # print(json_result.get('paging'))

