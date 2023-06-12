# Use Xpath and Session

import requests
from lxml.html import fromstring, tostring

def main():
    # Use session
    session = requests.Session()

    response = session.get("https://news.nate.com/total")

    # Get a dictionary of img url
    urls = scrape_news_list_page(response)

    for img, url in urls.items():
       print("img: ", img, "url: ", url)

def scrape_news_list_page(response):
    urls = dict()
    root = fromstring(response.content)

    for a in root.xpath('//ul[@class="coverStory"]/li/a[@class="link"]'):
        img, url = extract_contents(a)
        urls[img] = url
    
    return urls

def extract_contents(dom):
    link = dom.get("href")
    img = dom.xpath('./span[@class="thumb"]/img')[0].get("src")
    return img, link

if __name__ == "__main__":
    main()