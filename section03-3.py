# Header with user-agent and referer should be created and included for ajax websites
# Get stock info from Daum
# Installed fake-useragent

import json
import urllib.request as req
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.ie)
print(ua.msie)
print(ua.chrome)
print(ua.safari)
print(ua.random)

# Header info
myheaders = {
    'User-agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

# Request
url = "https://finance.daum.net/api/search/ranks?limit=10"
res = req.urlopen(req.Request(url, headers=myheaders)).read().decode('UTF-8')
print('res: ', res)

# Transform str to json
rank_json = json.loads(res)['data']
for item in rank_json:
    print('rank: {}, price: {}, company: {}'.format(item['rank'], item.get('tradePrice'), item['name']))