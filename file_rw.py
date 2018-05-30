#!/usr/bin/python3
# -*- conding: utf-8 -*-

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt', 'r')
content = baconFile.read()
baconFile.close()
print('content is \n' + content)


