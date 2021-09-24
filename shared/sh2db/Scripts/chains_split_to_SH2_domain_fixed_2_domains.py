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
                counter = 0
                for i in table[table['PDB ID'] == pdb]["New_PDB_start"].unique():
                    for j in table[table['PDB ID'] == pdb]["New_PDB_stop"].unique():
                        counter += 1
                        protein_pole = ''
                        if counter == 1:
                            protein_pole = "N"
                        if counter == 2:
                            protein_pole = "C"  
                        split_SH2D = 'pdb_selres -'+str(i)+':'+str(j)+' /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'.pdb > /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2_'+protein_pole+'.pdb'
                        os.system(split_SH2D)
                        #os.system('mv '+pdb+'_'+chain+'_SH2.pdb /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                        if x%1 == 0:
                            print("Already splitted for SH2 domain {} PDB entries".format(x))
                        x += 1
                            
print("Done with selecting resiudes")
