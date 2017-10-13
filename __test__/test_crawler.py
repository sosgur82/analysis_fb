import analysis_fb.collection.crewler as crawler

pagename = 'jtbcnews'
since = '2017-10-01'
until = '2017-10-01'

items = [
('jtbcnews', '2017-10-01', '2017-10-13')]

for pagename, since, until in items:
    crawler.crawling(pagename,since,until)
