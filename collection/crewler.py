from .api import api

def crawling(pagename, since, until):
    for posts in api.fb_fetch_posts(pagename,since,until):
        print(posts)
