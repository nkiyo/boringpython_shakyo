#!/usr/bin/python3
# -*- coding: utf-8 -*-

# read 1つのstringとして読込
helloFile = open('/home/Nakah/work/boringpy/sample.py')
helloConent = helloFile.read()
print(helloConent)
print(type(helloConent))
helloFile.close()

# readlines 行単位で stringのlistとして読込
helloFile2 = open('/home/Nakah/work/boringpy/sample.py')
helloConent2 = helloFile2.readlines()
print(helloConent2)
print(type(helloConent2))
helloFile2.close()


