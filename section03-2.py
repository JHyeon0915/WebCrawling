# Get RSS

import urllib.request
import urllib.parse

# 행정안전부
API = "https://mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012"
params = []

for num in range(1000,1014):
    params.append(dict(ctxDc=num))

for c in params:
    # Encode URL
    params = urllib.parse.urlencode(c)
    
    # Complete URL
    url = API + "?" + params

    # Get resposne
    res_data = urllib.request.urlopen(url).read()

    # Decode Response
    contents = res_data.decode("UTF-8")
    print(contents)