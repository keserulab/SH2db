#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio.PDB import PDBList
import sys
import os

table = pd.read_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_struct.csv')
print(table.head())

print("TABLE READING HAS FINISHED")

x = 0
print("Categories {}".format(",".join(table["Category"].unique())))
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[(table["Gene name"] == gene) & (table["Category"] == cat)]["PDB ID"].unique():
            change_permission = 'chmod 777 /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb'
            os.system(change_permission)
            if x%1 == 0:
                print("Already changed the permissions for {} PDB files".format(x)) 
            x += 1

