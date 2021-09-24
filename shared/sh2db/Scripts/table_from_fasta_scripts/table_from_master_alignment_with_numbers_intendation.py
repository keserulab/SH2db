
import sys
import os
import csv
import pandas as pd

#with open('/home/takacsg/Documents/SH2DB/sh2_master.fasta') as fasta:
#    line = fasta.readline()
#print(line, "\n", "Succesful fasta file read.")

#table = pd.read_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv')
#print(table.head())

with open('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv') as table:
    numbers = {}
    for line in table:
        line = line.split(',')
        #print("this is the line", line)
        ID = line[6].strip()
        #print(ID + "__END")
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
            current_ID = current_ID.split('|')[0].strip()
            #print(current_ID + "__END")
        else:
            #lista = len(x) # x is the original sequence (with gaps)
            print(current_ID, ',', ','.join(x)) # this will give the comma separated sequence with gaps
            lista2 = [] # that will give the residue numbers
            non_gap = False # It should remain False until y = "-" (gap)
            counter = 0
            lista2.append(" ") # Added because ID-s are the first cells of rows
            try: counter_target = int(numbers[current_ID][1]) - int(numbers[current_ID][0]) 
            except KeyError: counter_target = 10000
            print(counter_target)
            for y in x:
                #print("Y: " + y)
                #print("Current ID: " + current_ID + "_END")
                if non_gap: # non_gap false -> y = word from the sequence
                    if counter == counter_target:
                        lista2.append(numbers[current_ID][1].rstrip())
                        print('1')
                        break
                    try:
                        #print("Entered try1")
                        lista2.append(int(numbers[current_ID][0].strip()) + counter)
                        #print('2')
                    except KeyError:
                        #print("Szarság van") 
                        continue
                    counter += 1
                elif y != '-': # y is not equal with gap (-) --> y is a word from the sequence -> i should count them and print numbers behind them
                    non_gap = True
                    print('3')
                    try:
                        #lista2.append(numbers[current_ID][0])
                        lista2.append(numbers[current_ID][0] + counter)
                        print('4')
                    except:
                        print('5')
                    counter += 1
                elif y == '-': # y is a gap in the seqs -> i do not increase the counter, do not print behind them numbers - just a space character 
                    print('6')
                    lista2.append(" ")
                    continue
            print(','.join(lista2))
  
