#!/usr/bin/python
import requests
import datetime as dt
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
t = dt.datetime.today()
fname = f'{dir_path}/csv/{t.year}_{t.month}.csv'
url = "https://www.olcc.state.or.us/pdfs/NumericPriceListCurrentMonth.csv"
response = requests.get(url)
if response.status_code == 200:
    with open(fname, 'wb') as file:
        file.write(response.content)
else:
    print('Failed to download OLCC price list. Status code:', response.status_code)

