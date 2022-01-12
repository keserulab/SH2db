#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio.PDB import PDBList
import sys
import os

pfam = pd.read_csv('/home/takacsg/Documents/sh2db/data/pfam_table_recalculated_0830.csv', engine ='python')
print(pfam.head())

pfam.fillna(method='ffill', inplace = True)
pfam.head()

print("TABLE FILLING HAS FINISHED")
#table = table[:20]
#print("Slicing done")

x = 0
for i in range(len(pfam)) :
    
    cat = pfam.loc[i, "Category"]
    #gene =  pfam.loc[i, "Gene_col"]
    gene = pfam.loc[i, "Gene_domain"]
    gene_name = pfam.loc[i, "Gene_domain"]
    gene_name = gene_name.split('_')[0]
    chain =  pfam.loc[i, "PDB chain ID"]
    pdb = pfam.loc[i, "PDB ID"]
    pole =  pfam.loc[i, "Pole"]
    start = pfam.loc[i, "New_PDB_start"]
    stop = pfam.loc[i, "New_PDB_stop"]
    
    pdb_id = str(pdb+'_'+chain+'_SH2_'+pole)

    split_SH2D = 'pdb_selres -'+str(start)+':'+str(stop)+' /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene_name+'/'+pdb+'/'+pdb+'_1_'+chain+'.pdb > /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene_name+'/'+pdb+'/'+pdb+'_'+chain+'_SH2_'+pole+'.pdb'
    os.system(split_SH2D)
    '''print("PDB: ", pdb, ", POLE: ", pole)
    print('i :', i, ', j: ', j)'''
    #os.system('mv '+pdb+'_'+chain+'_SH2.pdb /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
    if x%1 == 0:
        print("Already splitted for SH2 domain {} PDB entries".format(x))
    x += 1
                            
print("Done with selecting resiudes")
