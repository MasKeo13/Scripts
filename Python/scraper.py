#!/usr/bin/python

import os
import os.path
import requests
from bs4 import BeautifulSoup

# get data
data = requests.get('https://www.pdga.com/tour/event/42362')

# load data
soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('table', { 'id': 'tournament-stats-5' })
tbody = leaderboard.find('tbody')
player = tbody.find('a')

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    name = tr.find_all('td')[2].text.strip()
    pdga = tr.find_all('td')[3].text.strip()
    rating = tr.find_all('td')[4].text.strip()
    par = tr.find_all('td')[5].text.strip()
    print(place, par, name, pdga, rating)
