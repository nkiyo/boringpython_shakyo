#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('OO', 20, 5)):
    print('### boxPrint(' + sym + ', ' + str(w) + ', ' + str(h) + ')')
    try:
        boxPrint(sym, w, h)
    except:
        print(traceback.format_exc())

