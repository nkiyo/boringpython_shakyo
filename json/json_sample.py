#! python3
# -*- encoding: utf-8 -*-

import json

stringOfJson = '["hoge" : 123]'
#stringOfJson = '["name": "Zophie", "isCat": true]'
#pythonValue = ['isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': null]

jsonDataAsPythonValue = json.loads(stringOfJson)
print(str(jsonDataAsPythonValue))
print(type(jsonDataAsPythonValue))

