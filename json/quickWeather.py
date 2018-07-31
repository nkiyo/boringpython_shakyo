#! python3
# -*- encoding: utf-8 -*-

import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py appid')
    sys.exit()
my_appid = ' '.join(sys.argv[1:])
#print(location)

# 現在の天気
api_url = 'http://api.openweathermap.org/data/2.5/weather'
#response = requests.get(url = api_url, params = dict(q = 'kobe', appid = my_appid))
#response.raise_for_status()
#jsonVal = json.loads(response.text)
#print('current weather is ... \n' + str(jsonVal) + '\n\n')

# 今後5日間の予報 3時間間隔
# 現在の天気
api_url = 'http://api.openweathermap.org/data/2.5/forecast'
response = requests.get(url = api_url, params = dict(q = 'kobe', appid = my_appid))
response.raise_for_status()
jsonVal = json.loads(response.text)
forecasts = jsonVal['list']
print(str(forecasts))
for idx, f in enumerate(forecasts):
    #print('f[' + str(idx) + '] is '+ str(f.main.weather.main) + '\n\n')
    #print('f[' + str(idx) + '] is '+ str(f.dt) + '\n\n')
    #print('f[' + str(idx) + '] is '+ str(f[dt]) + '\n\n')
    print('f[' + str(idx) + '] is '+ str(f['dt']))
    print('f[' + str(idx) + '] is '+ str(f['main']))
    #print(type(f))
    # TODO dt => readable
#print('\n\nforecast is ... \n' + str(jsonVal) + '\n\n')

# TODO Load JSON into a python variable

