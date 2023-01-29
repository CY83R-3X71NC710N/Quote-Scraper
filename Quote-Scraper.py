import random
from bs4 import BeautifulSoup
import csv

URL = "http://quotes.toscrape.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup.find_all(class_='quote')

def get_random_quote():
quote = random.choice(quotes)
return quote.find(class_='text').get_text() + ' - ' + quote.find(class_='author').get_text()

def save_to_csv(quote):
with open('quotes.csv', mode='a') as file:
writer = csv.writer(file)
writer.writerow([quote])

random_quote = get_random_quote()
print(random_quote)
save_to_csv(random_quote)
