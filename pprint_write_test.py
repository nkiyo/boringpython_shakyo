#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
f = open('myCats.py', 'w')
f.write('cats = ' + pprint.pformat(cats) + '\n')
f.close();


