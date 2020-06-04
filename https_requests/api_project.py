import requests
import pyfiglet
from termcolor import colored
from random import choice

url = "https://icanhazdadjoke.com/search"

message = pyfiglet.figlet_format("Dad Joke API")
message = colored(message, color='cyan')
print(message)
user_term = input('let me tell you a joke! Give me a topic!: ')
response = requests.get(
    url, headers={'Accept': "application/json"}, params={"term": user_term, "limit": 1}).json()

results = response["results"][0]

num_jokes = response["total_jokes"]

if num_jokes > 1:
    print(f"there are {num_jokes} jokes about {user_term}s!")
    print(results["joke"])
elif num_jokes == 1:
    print(f"there is {num_jokes} joke about {user_term}s!")
    print(results["joke"])
else:
    print(f"there is no jokes with {user_term} in it....")
