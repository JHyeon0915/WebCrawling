# Get method data communications
# Urlparse is very important in get method

import urllib.request 
from urllib.parse import urlparse

# Request 1
url = "http://www.encar.com"
mem = urllib.request.urlopen(url)

print('type: {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('stastus: {}'.format(mem.status))
print('header: {}'.format(mem.getheaders()))
print('read: {}'.format(mem.read(100).decode('utf-8'))) # Read 100bytes in utf-8 format
print('parse: {}'.format(urlparse('http://www.encar.co.kr')))
print('parse: {}'.format(urlparse('http://www.encar.co.kr?test=test').query))

# Request 2
API = "https://api64.ipify.org"
values = {
    'format': 'json'    # Can be test or jasonp too
}

print('before param: {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param: {}'.format(params))

URL = API + "?" + params
print("url: {}".format(URL))

# Reading response data
data = urllib.request.urlopen(URL).read()
text = data.decode('UTF-8')
print('response: {}'.format(text))