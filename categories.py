import re
url = 'https://www.olcc.state.or.us/pdfs/category_price_list.pdf'
#TODO: Use requests to get the pdf and pdfminer to extract the text
#      without saving either file

# The categories are in alphebetical order
cat = ['BRANDY / COGNAC', 'CACHACA', 'CANADIAN', 'COCKTAILS', 'CORDIALS',
       'DOMESTIC WHISKEY', 'GIN', 'IRISH', 'MEZCAL', 'NEUTRAL GRAIN SPIRIT',
       'OTHER IMPORTED WHISKY', 'RUM', 'SCOTCH', 'TEQUILA', 'VODKA', 
       'UNKNOWN']

def extract(fname):

    ci = 0 # category index
    bcat = {}

    with open(fname, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if cat[ci + 1] in line:
                ci += 1
            # All the item codes are 11 digits, starting with 999
            elif re.match('999[0-9]{8}', line):
                bcat[int(line)] = ci
    return bcat


if __name__ == '__main__':
    bottles = extract('categories.txt')
    print(len(bottles))
    print(bottles[99900511575])
        
