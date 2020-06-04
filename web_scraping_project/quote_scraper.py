import requests
from bs4 import BeautifulSoup

from random import choice
from csv import DictWriter,DictReader

BASE_URL = "http://quotes.toscrape.com/"

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess= ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
        remaining_guesses-=1
        if guess.lower() == quote["author"].lower():
            print("You guessed correctly!")
            break
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birthplace = soup.find(class_="author-born-location").get_text()
            print(f"here is a hint: The author was born on {birth_date}  {birthplace}")
        elif remaining_guesses == 2:
            print(f"here is a hint: The author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"here is a hint: The author's last name starts with {last_initial}")
        else: 
            print(f"sorry you ran out of guesses! The answer was {quote['author']}")

            
    again = ''
    while again.lower() not in ('y','yes','n','no'):
        again = input("Would you like to play again?: (y/n)\n" )
    if again.lower() in ('yes','y'):
        return start_game(quotes)
    else:
        print("ok goodbye! thanks for playing!")
start_game(quotes)