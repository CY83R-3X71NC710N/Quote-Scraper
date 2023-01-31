import random
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://quotes.toscrape.com"

def get_random_quote():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    quotes = soup.find_all(class_='quote')
    quote = random.choice(quotes)
    return quote.find(class_='text').get_text() + ' - ' + quote.find(class_='author').get_text()

def save_to_csv(quote, recursion_limit=5):
    with open('quotes.csv', mode='r') as file:
        reader = csv.reader(file)
        quotes_in_file = [row[0] for row in reader]
    if quote in quotes_in_file:
        if recursion_limit == 0:
            raise Exception("Recursion limit reached")
        return False
    with open('quotes.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([quote])
    return True

while True:
    try:
        random_quote = get_random_quote()
        print(random_quote)
        success = save_to_csv(random_quote)
        if success:
            break
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
