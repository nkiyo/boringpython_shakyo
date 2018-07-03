#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "lxml")
elems = exampleSoup.select('#author')
print(type(elems))
