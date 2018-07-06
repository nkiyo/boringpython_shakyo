#! python3
# -*- encoding: utf-8 -*-

import requests, sys, bs4
from subprocess import call

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
links = soup.select('.r a')
numOpen = min(5, len(links))
for i in range(numOpen):
    url = 'http://google.com' + links[i].get('href')
    call(["cygstart", url])


