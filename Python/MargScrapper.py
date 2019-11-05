#!/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup

# get data
data = requests.get('https://pdasu1.internal.nextcapital.html')

# load data
soup = BeatifulSoup(data.text, 'html.parser')

#get data looking for each tr
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]

    print(values)
