"""
**requests module **

-lets us make HTTP request from our Python code!
-installed using pip
-usedful fro webscraping/crawling, grabbing data from other APIs, etc
-

"""
import requests

url = "http://google.com"
response = requests.get(url)
print(f"your request to {url} came back w/ status code {response.status_code}")
