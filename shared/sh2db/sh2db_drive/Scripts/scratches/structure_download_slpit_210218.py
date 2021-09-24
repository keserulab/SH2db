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


# ### Creating the needed folders:
# 
# Catergory folders / folders for every pdb entry

# creating the category folders:
x = 0
for cat in table["Category"].unique():
    os.system('mkdir -p /home/takacsg/Documents/SH2DB/Stuctures/'+cat+'/')
# -p : no error if existing, make parent directories as needed
print("CATEGORY FOLDER ARE READY")

# creating the pdb folders (inside the category folders:Gene name):
x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
         os.system('mkdir -p /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/')
         if x%1 == 0:
             print("Already created folders {} PDB entries".format(x))
         x += 1



print("GENE NAME FOLDERS INSIDE THE CATEGORY FOLDERS ARE READY")

# 5%2=1 !!

# creating the pdb folders (inside the category folders:
x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            os.system('mkdir -p /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
            if x%1 == 0:
                print("Already created folders {} PDB entries".format(x))
            x += 1

print("ALREADY CREATED THE FOLDER SYSTEM.")

# ## 2. Download the structures (in PDB format)

# ## `pdb_fetch`:

x = 0
print("Categories {}".format(",".join(table["Category"].unique())))
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[(table["Gene name"] == gene) & (table["Category"] == cat)]["PDB ID"].unique():
            fetch_pdb = 'pdb_fetch '+pdb+' > //home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%1 == 0:
                print("Already fetched {} PDB entries".format(x)) 
            x += 1

print("ALREADY FETCHED ALL THE PDB ENTRIES.")


# ## 3. Split the protein into chains by pdb-tools `pdb_splitchain`
# 
# - pdb_splitchain: splits a pdb file into several, each containing one chain.
# - output file names will be: pdbid_A.pdb pdbid_B.pdb
# - usage: pdb_splitchain 2cr4.pdb



for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                split_pdb = 'pdb_splitchain home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb' ## > /home/agnes/Documents/STAT/Structures/'+cat+'/'+pdb+'/' ## +pdb+'_'+chain+'.pdb'
                os.system(split_pdb)
                os.system('mv '+pdb+'_'+chain+'.pdb home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                if x%1 == 0:
                    print("Already fetched {} PDB entries".format(x))
                x += 1


# ## 4. Split out the SH2-domain from the pdb files of the chains by `pdb_selres`:

# ### pdb_selres | Selects residues by their index, piecewise or in a range.
# 
# The range option has three components: start, end, and step. Start and end
# are optional and if ommitted the range will start at the first residue or
# end at the last, respectively.
# 
# #### Usage:
#     python pdb_selres.py -[resid]:[resid]:[step] <pdb file>
# 
# #### Example:
#     - python pdb_selres.py -1,2,4,6 1CTF.pdb # Extracts residues 1, 2, 4 and 6
#     - python pdb_selres.py -1:10 1CTF.pdb # Extracts residues 1 to 10
#     - python pdb_selres.py -1:10,20:30 1CTF.pdb # Extracts residues 1 to 10 and 20 to 30
#     - python pdb_selres.py -1: 1CTF.pdb # Extracts residues 1 to END
#     - python pdb_selres.py -:5 1CTF.pdb # Extracts residues from START to 5.
#     - python pdb_selres.py -::5 1CTF.pdb # Extracts every 5th residue
#     - python pdb_selres.py -1:10:5 1CTF.pdb # Extracts every 5th residue from 1 to 10
# 
# python pdb_selres.py -1:10:5 1CTF.pdb - de így csak kiírja a terminalba --> file-ba kell menteni! 



for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                    for i in table[table['PDB ID'] == pdb]["Res_start"].unique():
                        for j in table[table['PDB ID'] == pdb]["Res_stop"].unique():
                            #os.system('cd /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                            split_SH2D = 'python /home/takacsg/anaconda3/lib/python3.8/site-packages/pdbtools/pdb_selres.py -'+i+':'+j+' /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'.pdb  > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+pdb+'/'+pdb+'_'+chain+'_sH2.pdb'
                            os.system(split_SH2D)
                            os.system('mv '+pdb+'_'+chain+'_sH2.pdb home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                            if x%1 == 0:
                                print("Already fetched {} PDB entries".format(x))
                            x += 1

"""
pfam_table.head()

split_SH2D = 'pdb_selres -20:100 home/takacsg/Documents/SH2DB/Structures/SigRed/3BP2/2CR4/2CR4_A.pdb  > home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+pdb+'/'+pdb+'_'+chain+'_sH2.pdb'
os.system(split_SH2D)

os.system(' /home/takacsg/anaconda3/lib/python3.8/site-packages/pdbtools/pdb_selres.py -20:100 /home/takacsg/Documents/SH2DB/Structures/3BP2/2CR4/2CR4_A.pdb >home/takacsg/Documents/SH2DB/Structures/SigRed/3BP2/2CR4/2CR4_A_SH2.pdb')
"""

