"""
Requests + Beautiful soup example

Goals 
- scrape data into a csv file
-goal: Grab all links from Rithm School blog
-data: store URL, Anchor tag text, and date
"""
import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("web_scraping/blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title","link", "date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])