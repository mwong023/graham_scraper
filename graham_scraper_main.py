import requests
from bs4 import BeautifulSoup
import pickle
import os
import subprocess

# run essay_htmls.py
subprocess.call(["python3", "essay_htmls.py"])

# create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# load the list of essay html links into variable "articles"
with open('staging/articles_list.pkl', 'rb') as f:
    articles = pickle.load(f)

# skip these html links from scraping
skip_list = [
    'https://sep.turbifycdn.com/ty/cdn/paulgraham/acl1.txt?t=1713986320&' ## different indexing, don't want to bother
    ,'https://sep.turbifycdn.com/ty/cdn/paulgraham/acl2.txt?t=1713986320&' ## different indexing, don't want to bother
    ,'rss.html' ## nothing useful
    ,'index.html' ## nothing useful
]

for article in articles:
    if article in skip_list: ## skip the rest of commands in the for loop if the html is in the skip list
        continue
    else:
        url = f"https://www.paulgraham.com/{article}" 

    response = requests.get(url) 
    #response.raise_for_status() ## i don't really know whether i want this or not ...

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find_all("table")[1].find("tr").find("img").get('alt') ## gets the title, which is an alt image
    content = soup.find_all("table")[1].find("tr").get_text() ## gets the text of the essay
    blog_formatted = f"{title}\n{article}\n\n{content}\n\n" ## each article gets formatted with the title, html link, and then the contents of the essay

     # create a safe filename from the title
    filename = "data/" + "".join(x for x in title if x.isalnum()) + ".txt"

    # write the blog_formatted contents into a new file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(blog_formatted)