# Session(Cookies)
# www.httpbin.org

import requests

# Activate session
s = requests.Session()

# Get cookies
r1 = s.get('https://www.httpbin.org/cookies', cookies={'name': 'kim1'})
print(r1.text)

# Set cookies (RESTful API)
r2 = s.get('https://www.httpbin.org/cookies/set', cookies={'name': 'kim2'})
print(r2.text)

# User-Agent
url = 'https://www.httpbin.org'
headers = {'user-agent': 'nice-man_1.0.0.win10_ram16_home_chrome'}

# Send headers
r3 = s.get(url, headers=headers)
print(r3.text)

# Status code
print('status code: {}'.format(r1.status_code))
print('ok : {}'.format(r2.ok))

# Close session
s.close()

# With statement is recommended for files, DB and HTTP
# For readibility and automatic resource closing
with requests.Session() as s:
    r = s.get('https://www.google.com')
    print(r.text)
    print(r.ok)