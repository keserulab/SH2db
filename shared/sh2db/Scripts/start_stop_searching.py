import sys
import os
import pandas as pd
import numpy as np

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
"""
Recommended usage: python3 start_stop_searching.py > start_stop_points.txt
"""
# Create a dictionary for save the SH2-domains first 5 residues: 

start_dict = {}

def value_prepare_start(x):
    position = 0
    y = []
    x = x.strip('-')
    #print(x)
    for i in x:
        if i != '-':
            #position += 1
            y.append(i)
            if len(y) == 5:
                y = "".join(y)
                return y
            
    
with open('/home/takacsg/Documents/sh2db/data/sh2_master_edited.fasta') as fasta:
    for x,line in enumerate(fasta, 0):
        #print(x)
        if x%2 == 0:
            ID = line.rstrip()
            ID = ID.split('>')[1]
            ID = ID.split('|')[0]
        if x%2 != 0:
            value = line.rstrip()
            value = value_prepare_start(value)
            value = value[:10]
            start_dict[ID] = value

        
print("START DICTIONARY", "\n", start_dict)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# Create a dictionary for save the SH2-domains last 5 residues:

stop_dict = {}

def value_prepare_stop(x):
    position = 0
    y = []
    x = x.strip('-')
    #print(x)
    for i in x[::-1]:
        if i != '-':
            #position += 1
            y.append(i)
            if len(y) == 5:
                y = "".join(y)
                return y
            
    
with open('/home/takacsg/Documents/sh2db/data/sh2_master_edited.fasta') as fasta:
    for x,line in enumerate(fasta, 0):
        #print(x)
        if x%2 == 0:
            ID = line.rstrip()
            ID = ID.split('>')[1]
            ID = ID.split('|')[0]
        if x%2 != 0:
            value = line.rstrip()
            value = value_prepare_stop(value)
            value = value[:10]
            value = value[::-1]
            stop_dict[ID] = value

        
print("STOP DICTIONARY", "\n", stop_dict)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Importing the table:

filtered_table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv')
filtered_table.head()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

print("START POINTS:")

# Searching for the first residue numbers:

def starting_residues(aa_seqs, res):
    pos_count = 0
    pos = []
    matches = {}
    count = 0
    for i in aa_seqs:
        pos_count += 1
        residues = aa_seqs[pos_count : pos_count + len(res)]
        #print(residues)
        if residues == res:
            count +=1
            pos.append(pos_count)
            matches[res] = count
    return pos, matches
        
        
positions = []
for ID in filtered_table["Uniprot_ID"]:
    fasta = open('/home/takacsg/Documents/sh2db/FASTA/'+ID+'.fasta')
    seq_str = ''
    for line in fasta:
        if line.startswith('>'):    # skipping the lines which are not contain sequence
            continue
        else:
            seq_str += line.rstrip('\n')    # removing the new line charachters which present in the file - the sequences in the files are one, continuose sequence
        #print(seq_str)
        missing_genes = []
        start_res = {}
        for gene in filtered_table[filtered_table['Uniprot_ID'] == ID]['Gene name']: 
            if gene in start_dict.keys():
                aa_seq = seq_str
                res = start_dict[gene]
                pos, matches = starting_residues(aa_seq, res)
                
            else:
                missing_genes.append(gene)
    pos2 = []
    for k in pos:
        k += 1
        pos2.append(k)
    positions.append(pos2)
    print('pos: ', pos, '\n', 'matches: ', matches, '\n', 'missing: ', missing_genes,'\n',"positions: ", positions)


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# Searching for the last residue numbers:

# Residue number + 4 } It gives the first residues positions from matching of the five word long string.

print("STOP POINTS:")

def stop_residues(aa_seqs, res):
    pos_count = 0
    pos = []
    matches = {}
    count = 0
    for i in aa_seqs:
        pos_count += 1
        residues = aa_seqs[pos_count : pos_count + len(res)]
        #print(residues)
        if residues == res:
            count +=1
            pos.append(pos_count)
            matches[res] = count
    return pos, matches
        
        

for ID in filtered_table["Uniprot_ID"]:
    fasta = open('/home/takacsg/Documents/sh2db/FASTA/'+ID+'.fasta')
    seq_str = ''
    for line in fasta:
        if line.startswith('>'):    # skipping the lines which are not contain sequence
            continue
        else:
            seq_str += line.rstrip('\n')    # removing the new line charachters which present in the file - the sequences in the files are one, continuose sequence
        #print(seq_str)
        missing_genes = []
        start_res = {}
        for gene in filtered_table[filtered_table['Uniprot_ID'] == ID]['Gene name']:
            if gene in stop_dict.keys():
                aa_seq = seq_str
                res = stop_dict[gene]
                #print('seq: ', aa_seq)
                #print('res: ', res)
                pos, matches = stop_residues(aa_seq, res)
                #start_res[pos] = matches # matches egy dictionary; pos: list
            else:
                missing_genes.append(gene)
    print('pos: ', pos, '\n', 'matches: ', matches)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>