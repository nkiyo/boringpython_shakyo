#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print('num of pages : ' + str(pdfReader.numPages))

# Nページ目 テキスト抽出
#page = pdfReader.getPage(0)
page = pdfReader.getPage(1)
print(page.extractText())

