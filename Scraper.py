#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres URL strony z opiniami
url="https://www.ceneo.pl/76891706#tab=reviews"

#pobranie kodu HTTML strony z adresu URL
page  = requests.get(url)
page_tree = BeautifulSoup(page.text, 'html.parser')
print(page_tree.prettify())
#wybranie kodu  strony z fragmentow
opinions = page_tree.select("li.review-box")


#ekstrakcj SKLADOWYCH dla 1 opnii z listy

opinion = opinions[1]
id = opinion.select("li.review-box['data-entry-id']")
author = opinion.select('div.reviewer-name-line')
recomendation = opinion.select('div.product-review-summary > em')
stars = opinion.select('span.review-score-count')