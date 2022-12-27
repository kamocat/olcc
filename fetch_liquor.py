import requests
import datetime as dt

t = dt.datetime.today()
fname = f'csv/{t.year}_{t.month}.csv'
url = "https://www.olcc.state.or.us/pdfs/NumericPriceListCurrentMonth.csv"
response = requests.get(url)
if response.status_code == 200:
    with open(fname, 'wb') as file:
        file.write(response.content)
else:
    print('Failed to download OLCC price list. Status code:', response.status_code)

