#!/usr/bin/python3
import requests
import textwrap
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find_all(class_="story-heading")

for i in title:
    headlines = i.get_text()
    headlines = textwrap.fill(headlines, width=70).strip()
    print(headlines)
