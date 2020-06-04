"""
**Requests headers **
import requests 
response = requests.get("http://www.example.com", headers={
    "header1": "value1",
    "header2": "value2"
})

"""
import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={'Accept': "application/json"})
# print(response.text)
data = response.json()
print(type(data))
print(data["joke"])
