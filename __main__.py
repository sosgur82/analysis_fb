import collection
pagename = 'jtbcnews'
since = '2017-10-01'
until = '2017-10-01'
if __name__ == '__main__':
    items = [
        {'pagename':'jtbcnews', 'since':'2017-10-01', 'until':'2017-10-13'},
        {'pagename': 'chosun', 'since': '2017-10-01', 'until': '2017-10-13'},
    ]
    # collection
    for item in items:
       resultfile = collection.crawling(**item)
       item['resultfile'] = resultfile

    # analysis1
    for item in items:
        print(item['resultfile'])

    # visualization

