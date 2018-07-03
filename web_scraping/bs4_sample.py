#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")
print(type(noStarchSoup))
