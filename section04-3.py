# REST API
# GET, POST, DELETE, PUT(UPDATE, REPLACE(FETCH: UPDATE, MODIFY))
# Get and post all the status info using URL

import requests

# Get Example 1
s = requests.Session()
r = s.get('https://api.github.com/events')
r.raise_for_status()
#print(r.text)

# Get example 2: set cookies
jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'niceman', domain="httpbin.org", path='/cookies')
r = s.get('http://httpbin.org/cookies', cookies=jar)
#print(r.text)

# Get example 3
r=s.get('https://github.com',timeout=5)
#print(r.text)

# Post example 1
r = s.post('http://httpbin.org/post', data={'id':'test1', 'pw':'111'})
#print(r.text)

# Post exmple 2
payload1 = {'id':'test1', 'pw':'111'}
payload2 = (('id', 'test1'), ('pw', '111'))
r = s.post('http://httpbin.org/post', data=payload2)
#print(r.text)

# REST API example: PUT
r = s.put('http://httpbin.org/put', data=payload1)
#print(r.text)

# REST API example: DELETE
r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)

s.close()