import re
import requests
from pdfminer.high_level import extract_text
url = 'https://www.olcc.state.or.us/pdfs/category_price_list.pdf'

def fetch(fname):
    response = requests.get(url)
    if response.status_code == 200:
        with open(fname, 'wb') as file:
            file.write(response.content)
        print(f'Successfully downloaded {fname}')
    else:
        raise ConnectionError(f'HTTP code {response.status_code}')


# The categories are in alphebetical order
cat = ['UNCATEGORIZED', 
       'BRANDY / COGNAC', 'CACHACA', 'CANADIAN', 'COCKTAILS', 'CORDIALS',
       'DOMESTIC WHISKEY', 'GIN', 'IRISH', 'MEZCAL', 'NEUTRAL GRAIN SPIRIT',
       'OTHER IMPORTED WHISKY', 'RUM', 'SCOTCH', 'TEQUILA', 'VODKA', 
       'UNKNOWN']

def extract(fname):

    ci = 0 # category index
    bcat = {}

    text = extract_text(fname)
    lines = text.split('\n')
    print(f'Converted {fname} to {len(lines)} lines of text')

    for line in lines:
        # All the item codes are 11 digits, starting with 999
        if re.match('999[0-9]{8}', line):
            bcat[int(line)] = ci
        elif cat[ci + 1] in line:
            ci += 1
    return bcat


if __name__ == '__main__':
    bottles = extract('categories.pdf')
    print(f'Found {len(bottles)} bottles')
    x = 99900511575
    print(f'Bottle {x} is {cat[bottles[x]]}')
        
