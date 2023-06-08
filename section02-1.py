# urlretrieve(): 
# Copy the network object represented as URL for a local file
# Return the file name that is requested and request header

import urllib.request as req

img_url = 'https://ichef.bbci.co.uk/news/640/cpsprodpb/E172/production/_126241775_getty_cats.png'
html_url = 'http://google.com'

dest_path1 = 'C:/Users/noblelee/Desktop/python_crawl/destination/img.jpg'
dest_path2 = 'C:/Users/noblelee/Desktop/python_crawl/destination/index.html'

try:
    file1, header1 = req.urlretrieve(img_url, dest_path1)
    file2, header2 = req.urlretrieve(html_url, dest_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('file1 {}'.format(file1))
    print('file2 {}'.format(file2))