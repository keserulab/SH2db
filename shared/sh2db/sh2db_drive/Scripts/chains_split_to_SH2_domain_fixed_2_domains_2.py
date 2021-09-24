#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio.PDB import PDBList
import sys
import os

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_with_pdb_nums_domcol.csv', engine ='python')
print(table.head())

table.fillna(method='ffill', inplace = True)
table.head()

print("TABLE FILLING HAS FINISHED")
#table = table[:20]
#print("Slicing done")

x = 0
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                for pole in table[(table["PDB ID"] == pdb) & (table["PDB chain ID"] == chain)]["Pole"].unique():
                    for i in table[(table["PDB ID"] == pdb) & (table["PDB chain ID"] == chain) & (table["Pole"] == pole)]["New_PDB_start"].unique():
                        for j in table[(table["PDB ID"] == pdb) & (table["PDB chain ID"] == chain) & (table["Pole"] == pole)]["New_PDB_stop"].unique(): 
                            split_SH2D = 'pdb_selres -'+str(i)+':'+str(j)+' /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1_'+chain+'.pdb > /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1_'+chain+'_SH2_'+pole+'.pdb'
                            os.system(split_SH2D)
                            print(pdb)
                            if x%1 == 0:
                                print("Already splitted for SH2 domain {} PDB entries".format(x))
                            x += 1
                            
print("Done")
