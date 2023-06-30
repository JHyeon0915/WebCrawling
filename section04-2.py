# JSON

import json
import requests

s = requests.Session()

# Request 100 of JSON data
r = s.get('https://httpbin.org/stream/100', stream=True)
print(r.text)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    b = json.loads(line)    # Transform line to json(dictionary)
    for k, v in b.items():
        print('key: {}, value: {}'.format(k,v))

s.close()

# Another practice
# JSONPlaceholder
r = s.get('https://jsonplaceholder.typicode.com/todos/1')
print(r.headers)
print(r.text)
print(r.json())
print(r.json().keys())  # values() for values
print(r.content)    # Binary

s.close()