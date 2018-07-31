#!/bin/bash

wget "http://api.openweathermap.org/data/2.5/forecast?q=kobe&appid=11cc9613abd50a8d70090aa3c5d13968" -O forecast.json

# 全体を整形して表示
cat forecast.json | jq .



