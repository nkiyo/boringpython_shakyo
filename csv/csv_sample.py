#! python3
# -*- encoding: utf-8 -*-

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
#print(exampleData)
for line in exampleData:
    print('line is ' + str(line))
    for elem in line:
        print('elem is ' + elem)

