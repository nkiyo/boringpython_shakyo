#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import requests, bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "lxml")

# id=authorの要素リストを取得
elems = exampleSoup.select('#author')
print(type(elems)) # => class 'list'
print(elems[0].getText()) # タグに囲まれた部分だけ表示
print(str(elems[0])) # タグ全体を表示

# attributeとvalueの組を返す
print(str(elems[0].attrs))

# タグ名指定で項目取得
pElems = exampleSoup.select('p')
print(pElems)
for idx, e in enumerate(pElems):
    print(str(idx) + ': getTex() => ' + e.getText())

# 属性(attribute)名で値取得
spanElem = exampleSoup.select('span')[0]
print(str(spanElem.get('id'))) # 属性名に対応する値を返す
print(str(spanElem))
print(str(spanElem.attrs)) # {属性名 : 値} の組を出力

