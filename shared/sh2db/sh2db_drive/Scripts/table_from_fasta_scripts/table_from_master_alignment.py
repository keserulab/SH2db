
import sys
import os
import csv
import pandas as pd

with open('/home/takacsg/Documents/SH2DB/sh2_master.fasta') as fasta:
    line = fasta.readline()
print(line, "\n", "Succesful fasta file read.")

table = pd.read_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_struct.csv')
print(table.head())

table.fillna(method='ffill', inplace = True)
print(table.head())

"""numbers = {}
for line in table:
    ID = ','.split(line)[8]
    start =  ','.split(line)[10]
    stop = ','
    numbers[ID] = [start, stop]"""
    
    
my_file = []
n = 0
lista = []
with open('/home/takacsg/Documents/SH2DB/sh2_master.fasta') as fasta:
    for x in fasta:
        n += 1
        if n % 2 != 0:
            print(x)
            my_file.append(x)
        else:
            lista = ''.split(x)
            print(','.join(x))
            my_file.append(','.join(x))
    len(lista)

