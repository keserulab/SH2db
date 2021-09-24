import sys
import os
import pandas as pd
import numpy as np

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

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

        
print(start_dict)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Importing the table:

filtered_table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv')
filtered_table.head()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# Searching for the first residue numbers:

def starting_residues(aa_seqs, res):
    pos_count = 0
    pos = []
    matches = {}
    count = 0
    for i in aa_seqs:
        pos_count += 1
        residues = aa_seqs[pos_count : pos_count + len(res)] # This iterates over the sequence and take always 5 long string for the seqs and test that these two string section are whether matching?
        if residues == res: # if they matching ... 
            count +=1
            #pos_count = pos_count + 1
            pos.append(pos_count)
            matches[res] = count
    print("POS 1", pos, '\n', "MATCHES 1", matches) 
    return pos, matches
        
        
#positions = []
for ID in filtered_table["Uniprot_ID"]:
    fasta = open('/home/takacsg/Documents/sh2db/FASTA/'+ID+'.fasta')
    seq_str = ''
    for line in fasta:  # line: one line from the fasta file
        #print("LINE", line)
        if line.startswith('>'):    # skipping the lines which are not contain sequence
            print(line)
            continue
        else:
            seq_str += line.rstrip('\n')    # removing the new line charachters which present in the file - the sequences in the files are one, continuose sequence
        #print("SEQ_STR", seq_str)       # lines continously from the fasta file } actually this is the sequence in evaluable form 
        missing_genes = []
        start_res = {}
        for gene in filtered_table[filtered_table['Uniprot_ID'] == ID]['Gene name']: 
            if gene in start_dict.keys():
                aa_seq = seq_str
                res = start_dict[gene]
                pos, matches = starting_residues(aa_seq, res)   # POS: the number of the first matching aminoacid; MATCHES: gives the 5 word long string what should be matched with one part of the seq_str's string 
                #print("POS", pos, "\n", "MATCHES", matches)
            else:
                missing_genes.append(gene)

    print('pos: ', pos, '\n', 'matches: ', matches, '\n', 'missing: ', missing_genes)

#"positions: ", positions