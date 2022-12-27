#!/usr/bin/python
import requests
from datetime import datetime
from os import path

fname = path.dirname(path.realpath(__file__))
fname = path.join(fname, 'csv')

url = "https://www.olcc.state.or.us/pdfs/NumericPriceListCurrentMonth.csv"
response = requests.get(url)
if response.status_code == 200:
    date = response.headers['last-modified']
    # example date Thu, 01 Dec 2022 13:26:02 GMT
    t = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
    fname = path.join(fname, t.strftime('%Y_%m.csv'))
    with open(fname, 'w', newline='\r\n') as file:
        file.write(f"Modified {date}\r\n")
        file.write(response.text.replace('\n\n', ' '))
else:
    print('Failed to download OLCC price list. Status code:', response.status_code)

