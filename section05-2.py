# Download images from nate.com with BeautifulSoup
# The version of urllib is old one. It is just a practice. Use urllib3 later

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Initialize Header information
opener = req.build_opener()
# Info of User-Agent
opener.addheaders = [('User-agent', UserAgent().ie)]
req.install_opener(opener)

# Image URL
url = 'https://www.nate.com'
# quote = rep.quote_plus('호랑이')    # Search keyword
# url = base + quote

# Request
res = req.urlopen(url)
save_path = 'C:\\imagedown'     # the same as 'C:/imagedown'

# Exception for folder creation
try:
    # If the path does not exist, make one
    if not os.path.isdir(save_path):
        os.makedirs(os.path.join(save_path))
except OSError as e:
    print("folder creation failed.\n")
    print("folder name: ", e.filename)

    raise RuntimeError("System Exit")
else:
    print('Folder successfully created!')

# Initialize bs4
soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select('span.thumb > img')
print(img_list)

# Download imgs
for i, img in enumerate(img_list,1):
    print('\n\n')
    fullFileName = os.path.join(save_path, save_path + str(i) + '.png')

    # Download request
    req.urlretrieve('https:' + img['src'], fullFileName)

print("Images successfully downloaded")