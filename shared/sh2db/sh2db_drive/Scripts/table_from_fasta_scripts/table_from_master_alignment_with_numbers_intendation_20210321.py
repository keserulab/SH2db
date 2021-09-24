
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
        x = x.rstrip()
        n += 1
        if n % 2 != 0:
            current_ID = x.rstrip() # x = eg.: STAT6 
            current_ID = current_ID[1:] #.split('>')[1]
            current_ID = current_ID.split('|')[0]
            #print(current_ID)
        else:
            #lista = len(x) # x is the original sequence (with gaps)
            print(current_ID, ',', ','.join(x)) # this will give the comma separated sequence with gaps
            lista2 = [] # that will give the residue numbers
            non_gap = False # It should remain False until y = "-" (gap)
            counter = 0
            lista2.append(" ") # Added because ID-s are the first cells of rows
            try: counter_target = int(numbers[current_ID][1]) - int(numbers[current_ID][0])
            except KeyError: counter_target = 10000  
            for y in x:
                if non_gap:
                    #print('1 első if')
                    if counter == counter_target:
                        #lista2.append(numbers[current_ID][1].rstrip())
                        lista2.append('___')
                        break
                    
                    try:
                        start_point = (numbers[current_ID][0])
                        lista2.append(start_point + count)
                        print("belépett a try-ba kitlteni a két szám kztti cellákat csak nem csinált semmit :@ @ @")
                    except: continue
                    #print('2 if-en belül if')
                    counter += 1
                    continue
                elif y != '-':
                    #print('3 elif')
                    non_gap = True
                    counter += 1
                    try:
                        lista2.append(str(int(numbers[current_ID][0]) + counter))
                        #print(' try ')
                    except: continue
                elif y == '-':
                    lista2.append("_")
                    #print('4 2.elif')
                    continue
            print(','.join(lista2))
  
