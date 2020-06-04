"""
Getting started with beautiful soup
-to extract data from HTML, we'll use beautiful soup
-install with pip
-beautiful soup lets us navigate through HTML with Python
-beautiful soup does NOT download HTML - for this, we need the requests modules!


parsing and navigating HTML
-beautifulsoup(html_string, "html.parser") - parse HTML
-once parsed, there are several ways to navigate:
  - by tag name
  -useing find -returns one matching tag
  -using find_all - returns a list of matching tags 
navigating with CSS selectors 
select - returns a list of elements matching a CSS selector
**Selector Cheatsheet
-select by id of foo: #foo
-select by class of bar: .bar
-select children: div > p
-select descendents: div p
"""

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# d = soup.select("[data-example]")
# print(d)
# print(soup.findAll("div"))
# print(soup.findAll("li"))
# print(soup.findAll(class_="special"))
print(soup.select("#first"))
