# README

This app will scrape all of Paul Graham's essays. 

`essay_htmls.py` gets a list of all the html url's to loop through. It gets fed into `graham_scraper_main.py`.

`graham_scraper_main.py` will scrape all of the essays and drop them as .txt files in the `data/` folder.  

#### Exceptions

There are two essays that Paul wrote early on and hosted them somewhere else.  I didn't want to deal with another scraper for those so I decided to just skip them. 
'https://sep.turbifycdn.com/ty/cdn/paulgraham/acl1.txt?t=1713986320&' 
'https://sep.turbifycdn.com/ty/cdn/paulgraham/acl2.txt?t=1713986320&'

## Usage

```pip install -r requirements.txt```

``` python3 graham_scraper_main.py ```