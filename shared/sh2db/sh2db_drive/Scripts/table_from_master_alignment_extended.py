
import sys
import os
import csv
import pandas as pd
import argparse

"""
Recommended usage:
cat ../data/sh2_master_edited.fasta | python table_from_master_alignment_with_numbers_intendation_20210316.py ../data/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv
"""


parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter
        )
parser.add_argument(
    type=str, 
    dest='inputfile2'
    )
args = parser.parse_args()

inputfile2 = args.inputfile2

# with open(sys.stdin, "r") as fasta:
#     line = fasta.readline()
#print(line, "\n", "Succesful fasta file read.")

#table = pd.read_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv')
#print(table.head())

#with open('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv') as table:
with open(inputfile2) as table:
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
# with open(sys.stdin, "r") as fasta:
for x in sys.stdin:
    x = x.rstrip()
    n += 1
    if n % 2 != 0:
        current_ID = x.rstrip() # x = eg.: STAT6 
        current_ID = current_ID[1:] #.split('>')[1]
        current_ID = current_ID.split('|')[0]
        #print(current_ID)
    else:
        #lista = len(x) # x is the original sequence (with gaps)
        print(current_ID + ',' + ','.join(x)) # this will give the comma separated sequence with gaps
        lista2 = [] # that will give the residue numbers
        non_gap = False # It should remain False until y = "-" (gap)
        counter = 0
        lista2.append(" ") # Added because ID-s are the first cells of rows
        try: 
            counter_target = int(numbers[current_ID][1]) - int(numbers[current_ID][0])
            for y in x:
                if non_gap:
                    if counter == counter_target:
                        lista2.append(numbers[current_ID][1].rstrip())
                        break
                    if y != "-":
                        num = str(int(numbers[current_ID][0]) + counter)
                        lista2.append(num)
                        counter += 1
                        #continue
                    else:
                        lista2.append(" ")
                elif y != '-':
                    non_gap = True
                    counter += 1
                    try:
                        lista2.append(numbers[current_ID][0])
                    except: continue
                elif y == '-':
                    lista2.append(" ")
                    continue
            print(','.join(lista2))
        except KeyError: 
            #counter_target = 10000
            print(" No structure found ")
  
