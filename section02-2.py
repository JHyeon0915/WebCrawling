# 

import os
from dotenv import load_dotenv

import urllib.request as req
from urllib.error import URLError, HTTPError    # For exception handling

load_dotenv()
PATH = os.getenv('DEST_PATH')
path_list = [PATH + '/img.jpg',PATH + '/index.html']
target_list = ['https://img.freepik.com/free-photo/adorable-kitty-looking-like-it-want-to-hunt_23-2149167099.jpg?w=2000', 'http://google.com']

for i, url in enumerate(target_list):
    try:
        # Read web resonse info
        res = req.urlopen(url)
        contents = res.read()
        print("---------------------------------")

        # Print status info
        print('Header Info: {}'.format(i, res.info()))
        print('HTTP Status Code: {}'.format(res.getcode()))
        print("---------------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed")
        print("HTTPError code: ", e.code)
    except URLError as e:
        print("URL Error Reason: ", e.reason)
    # Success
    else:
        print("Download succeed.")