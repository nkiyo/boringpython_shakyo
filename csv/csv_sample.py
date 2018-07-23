#! python3
# -*- encoding: utf-8 -*-

import csv

# read csv
# '#'から始まるコメント行を自動的に読込スキップする方法不明
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' is ' + str(row))
    for elem in row:
        print('elem is ' + elem)

# write csv
outputFile = open('output.csv', 'w', newline = '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs' , 'bacon', 'ham'])
outputWriter.writerow(['Hello, world', 'eggs', 'bacon', 'ham'])
outElem = [1, 2, 3,141592, 4]
print(str(type(outElem))) # => 'list'
outputWriter.writerow(outElem)
outputFile.close()

