import pandas as pd
import sys
import os


table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_struct.csv')

#x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                print('/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2.pdb')
                #if x%1 == 0:
                #    print("Already printed {} paths".format(x))
                #x += 1
