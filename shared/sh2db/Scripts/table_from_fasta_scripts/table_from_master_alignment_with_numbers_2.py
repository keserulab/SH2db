
import sys
import os
import csv
import pandas as pd

with open('/home/takacsg/Documents/SH2DB/sh2_master.fasta') as fasta:
    line = fasta.readline()
#print(line, "\n", "Succesful fasta file read.")

table = pd.read_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv')
#print(table.head())

with open('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv') as table:
    numbers = {}
    for line in table:
        line = line.split(',')
        #print("this is the line", line)
        ID = line[6]
        start = line[11]
        stop = line[12]
        numbers[ID] = [start, stop]
    
    
n = 0
lista = []
with open('/home/takacsg/Documents/SH2DB/sh2_master.fasta') as fasta:
    for x in fasta:
        n += 1
        if n % 2 != 0:
            current_ID = x.rstrip() # x = eg.: STAT6 
            current_ID = current_ID[1:] #.split('>')[1]
            current_ID = current_ID.split('|')[0]
            #print(current_ID)
        else:
            lista = len(x) # x is the original sequence (with gaps)
            print(current_ID, ',', ','.join(x)) # this will give the comma separated sequence with gaps
            seq = x.strip('-')
            #seq2 = x[].split('-')
            len_seq = len(seq)
            print("len seq", len_seq)
            lista2 = [] # that will give the residue numbers
            for y in x:
                print('this is the y', y)
                if y == 0:
                    try:
                        lista2.append(numbers[current_ID][0])
                    except: continue 
                elif y == len_seq - 1:
                    try:
                        lista2.append(numbers[current_ID][1])
                    except: continue
                else:
                    lista2.append('')
            print(','.join(lista2))
                    

