import sqlite3
import csv
import os

con = sqlite3.connect('liquor.db')
cur = con.cursor()
#For testing, we're overwriting the data
cur.execute('DROP TABLE IF EXISTS bottles');
cur.execute('DROP TABLE IF EXISTS prices');

cur.execute('CREATE TABLE bottles(item INTEGER PRIMARY KEY,description NOT NULL,size,age,proof REAL, category INTEGER)')
cur.execute('CREATE TABLE prices(item INTEGER, price REAL, date)')

mydir = os.path.dirname(os.path.realpath(__file__))
mydir = os.path.join(mydir, 'csv')

filenames = next(os.walk(mydir), (None, None, []))[2]  # [] if no file
for f in filenames:
    f = os.path.join(mydir, f)
    with open(f, newline='\r\n', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, dialect='excel')
        print(f'Opened {f}')
        date = next(csvreader)
        header = next(csvreader)
        for row in csvreader:
            cur.execute('''INSERT INTO bottles (item, description, size, age, proof) 
                        VALUES (?,?,?,?,?)''', [row[i] for i in [1,3,4,5,6]])
            cur.execute('INSERT INTO prices VALUES (?,?,?)', [row[1],row[8],row[9]])


        con.commit()
print('Prices saved')

import categories as cat
cur.execute('CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, name NOT NULL)')
for i, val in enumerate(cat.cat):
    cur.execute('INSERT OR IGNORE INTO categories VALUES (?,?)', [i,val])
con.commit()
cat.fetch('tmp.pdf')
bottles = cat.extract('tmp.pdf')
for x in bottles:
    cur.execute('UPDATE bottles SET category = ? WHERE item = ?', [bottles[x], x])
con.commit()
print('Categories saved')


con.close()

    


