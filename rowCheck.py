####################
## original build ##
####################

import csv

reader = csv.reader(open('testcolumns.csv', 'r'))


for row in reader:
    if len(row) <= 10:
        print("Success! CSV has", len(row), "rows.")
    elif len(row) > 10:
        print("Error. CSV has", len(row), "rows.")
    break


########################################
## convert over for import re library ##
########################################


import re

csvfile = open(csvFileName,'r') ## found in row 38 of current version V9 of .py file ##

for row in csvfile:
    if len(row) <= 200:
        print("Success! CSV has", len(row), "rows.")
    elif len(row) > 200:
        print("Error. CSV has", len(row), "rows.")
    break