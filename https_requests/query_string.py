"""
** Query String
- a way to pass data to the server as part of a GET requests
-example: http//www.example.com/?key1=value1&key2=value2
"""
# example
import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, headers={'Accept': "application/json"}, params={"term": "cat", "limit": "1"})  # the params are what are part of the search query
# print(response.text)
data = response.json()
# print(type(data))
# print(data["joke"])
print(data["results"])
