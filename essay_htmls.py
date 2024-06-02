import requests
from bs4 import BeautifulSoup
import pickle
import os

## create staging folder if it doesn't exist
if not os.path.exists('staging'):
    os.makedirs('staging')

url = "https://www.paulgraham.com/articles.html"
response = requests.get(url)
response.raise_for_status()


# Create a BeautifulSoup object from the HTML content of the response. This object allows us to parse and navigate the HTML structure.
soup = BeautifulSoup(response.text, 'html.parser')

# this navigates the html and locates where to find all the html links to the essays
test = soup.find_all("td")[2].find_all("a")

href_values = []

for a in test:
    href = a.get('href')
    if href:
        href_values.append(href)

## save the list to a pkl file. This is useful for the next script to load the list of html links
with open('staging/articles_list.pkl', 'wb') as f:
    pickle.dump(href_values,f)

with open('staging/articles_list.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)
