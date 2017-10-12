from analysis_fb.collection.api import api

# api.fb_gen_url(pagename='jtbcnews',a=1,b=2,no=3, token='321321')
#print(url)
api.fb_fetch_posts('jtbcnews','2017-01-01', '2017-10-12')