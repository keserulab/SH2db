#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio.PDB import PDBList
import sys
import os

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/pfam_table_recalculated_0830.csv')
print(table.head())

print("TABLE READING HAS FINISHED")


# ## 3. Split the protein into chains by pdb-tools `pdb_splitchain`
# 
# - pdb_splitchain: splits a pdb file into several, each containing one chain.
# - output file names will be: pdbid_A.pdb pdbid_B.pdb
# - usage: pdb_splitchain 2cr4.pdb


x = 0
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                print('PDB', pdb)
                print('CHAIN', chain)
                split_pdb = 'pdb_splitchain /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1.pdb'# > /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'.pdb'
                #os.system('cd /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                #os.system('pwd')
                os.system(split_pdb)
                os.system('mv '+pdb+'_1_'+chain+'.pdb  /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                if x%1 == 0:
                    print("Already splitted {} PDB entries".format(x))
                x += 1

print('DONE WITH SPLITTING PDB STRUCTURES TO CHAINS')