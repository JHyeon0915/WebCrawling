# BeautifulSoup

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>My story</title>
    </head>
    <body>
        <h1>I'm h1</h1>
        <h2>I'm h2</h2>
        <p class="title"><b>My story</b></p>
        <p class="story">
            Once upon a time there were three little sisters
            <a href="http://example.come/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.come/lacie" class="sister" id="link2">Lacie</a>
            <a data-io="link3" href="http://example.come/little" class="sister" id="link2">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""

# Example 1
# bs4 initiation
soup = BeautifulSoup(html, 'html.parser')
print("soup's type: ", type(soup))
print('prettify: ', soup.prettify())

h1 = soup.html.body.h1
print('h1: ', h1)
p1 = soup.html.body.p
print("P1: ", p1)  # Get the first p element
p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling
print("P2: ", p2)

# Print only text in an element
print('h1 >> ', h1.string)
print('p >> ', p1.string)   # <b> tag is ignored

# Check available functions
print(dir(p2))
print(p2.next_element)

# Example 2 (Find, Find_all)
soup2 = BeautifulSoup(html, 'html.parser')
link1 = soup2.find_all('a', limit=2)
print(link1)
print(type(link1))

# Multiple conditions
link2 = soup2.find_all('a', {'class':'sister'}, string=['Elsie', 'Title'])
print(link2)

# find(): the first element that meets the conditions
link3 = soup.find('a')
print(link3)
print(link3.string)
print(link3.text)

# Example 3(selelct, select_one)
# using css selectors -> select, select one, 
# Using tags -> find, find all

link4 = soup.select_one('p.title > b')  # select_one이 더 전문가스러움
print(link4)
link5 = soup.select('a#link2')
print(link5)

link7 = soup.select_one("a[data-io='link3']")   # Use [] when neither id nor class name
print(link7)

# Select
link8 = soup.select('p.story > a')
print(link8)

link9 = soup.select('p.story > a:nth-of-type(2)')   # Get second 'a' data under p.story
print(link9)

link10 = soup.select('p.story')
print(link10)

for t in link10:
    temp = t.find_all('a')
    if temp:
        for v in temp:
            print(v.string)
    else:
        print('none')