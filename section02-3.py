# pip install cssselect, requests, lxml


import requests
import lxml.html

def main():
    # Objects that's gonna be scrapped
    response = requests.get("https://www.nate.com/")

    urls = scrape_news_list_page(response)

    for url in urls:
       print(url)

def scrape_news_list_page(response):
    urls = []
    root = lxml.html.fromstring(response.content)
    print(root)
    for a in root.cssselect('.type_text li a'):
        url = a.get('href')
        urls.append(url)
    
    return urls
        

if __name__ == "__main__":
    main()