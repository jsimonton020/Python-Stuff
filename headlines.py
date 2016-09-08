#!/usr/bin/python3
import json
import requests
import textwrap
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find_all(class_="story-heading")

headlines_list = []

for i in title:
    headlines = i.get_text().strip()
    headlines_list.append(headlines)
    print(headlines)

with open('headlines.json', 'w') as w:
    json.dump(headlines_list, w, indent=4)
