#! python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code)
print(len(res.text))

