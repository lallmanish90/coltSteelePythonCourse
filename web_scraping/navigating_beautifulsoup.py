"""
Navigating with beautiful soup
-parent/parents
-contents
-next_sibling / previous_siblings 
            Via Searching  #can take in a string as an argument 
-find_parent / find_next_parent, find_previous_parent
-find_next_sibling / find_previous_siblings
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
    <li class="special" id ="this_id>This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#data = soup.body.contents[1].find_next_sibling()
data = soup.body.find("li").find_previous_sibling
# data = soup.body.find("li").find_parent
# data = soup.body.find("li").find_parent
print(data)
help(soup)