from urllib.parse import urlencode

ACCESS_TOKEN = '%s|%s' %('1795668674069712','c70756c28d2a49df476cd334dc357892')
BASE_URL_FB_API = 'https://graph.facebook.com/v2.10'
LIMIT_REQUEST=20

def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    return '%s/%s/?%s' % (base, node, urlencode(params))


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=pagename + "/posts",
        fields = 'id,message,link,name,type,shares,\
                  created_time,reactions.limit(0).summary(true),\
                  comments.limit(0).summary(true)',
        since = since,
        until=until,
        limit=LIMIT_REQUEST,
        access_token=ACCESS_TOKEN)
    print(url)

