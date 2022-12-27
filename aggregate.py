import sqlite3 as sq
import csv
import os

mydir = os.path.dirname(os.path.realpath(__file__))
mydir = os.path.join(mydir, 'csv')

filenames = next(os.walk(mydir), (None, None, []))[2]  # [] if no file
f = os.path.join(mydir, filenames[1])
with open(f, newline='\r\n', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, dialect='excel')
    print(f'Opened {f}')
    date = next(csvreader)
    header = next(csvreader)
    for row in csvreader:
        print(row[3])
    


