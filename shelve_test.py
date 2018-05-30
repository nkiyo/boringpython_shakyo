#!/usr/bin/python3
# -*- conding: utf-8 -*-
import shelve

#print(shelve.__file__)

# ファイル出力
sf = shelve.open('mydata')
cats = ['zophie', 'pooka', 'simon']
sf['cat'] = cats
dogs = ['aaa', 'bbbb', 'cccc']
sf['dog'] = dogs
sf.close()

# ファイル読込
sf = shelve.open('mydata')
# key 一覧表示
keys = list(sf.keys())
print(keys)
# value 一覧表示
vals = list(sf.values())
print(vals)
sf.close()

