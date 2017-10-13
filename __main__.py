import collection
import analyze

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

    # analysis
    for item in items:
        data = analyze.json_to_str(item['resultfile'],'message')
        item['count'] =  analyze.count_wordfreq(data)


    # visualization
    for item in items:
        count = item['count']
        print(count)
