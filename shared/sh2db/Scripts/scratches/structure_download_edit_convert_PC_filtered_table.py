#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio.PDB import PDBList
import sys
import os


# # Tasks:
# 0. 1 pár PDB entry letöltése
# 1. láncokra szedni a fehérjét
# 2. A láncokat tartalmazó pdb formátumot átalakítani fasta formátummá. (pdb-tools: pdb_to_fast function)
# 3. Illesztés - SH2 domén keresése (biopython package segítségével)
#     https://biopython.org/wiki/AlignIO?fbclid=IwAR1Wx2DEvgfn8xzK4y6Pc-m0keJ39iTDJsRaFTA664A2ZfVTMDhkrhNsutE
# 4. SH2-domént külön PDB file-ba kimenteni.
# 
# PDB-tools page: http://www.bonvinlab.org/pdb-tools/

# ## 1. Read in the tables which contains the pdb id's:

table = pd.read_csv("table_uniprot_new_start_stop.csv")
table.head()


table.fillna(method='ffill', inplace = True)
table.head()

print("Read in & filling up ready.")
"""
# ### Creating the needed folders:

# creating the pdb folders (inside the category folders:
x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            os.system('mkdir -p /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
            if x%1 == 0:
                print("Already made folders for {} PDB IDs".format(x)) 
            x += 1
# make the folders for kinases (new folder for every PDB ID)

print("PDB folders are ready")

# ## 2. Download the structures (in PDB format)

# ## `pdb_fetch` on the table slices:

x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb'
            os.system(fetch_pdb)
            if x%1 == 0:
                print("Already fetchd {} PDB entries".format(x)) 
            x += 1

# ## 3. Split the protein into chains by pdb-tools `pdb_splitchain`
# 
# - pdb_splitchain: splits a pdb file into several, each containing one chain.
# - output file names will be: pdbid_A.pdb pdbid_B.pdb
# - usage: pdb_splitchain 2cr4.pdb

x = 0                    
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                split_pdb = 'pdb_splitchain /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb' 
                os.system(split_pdb)
                os.system('mv '+pdb+'_'+chain+'.pdb /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                if x%1 == 0:
                    print("Structure splitting for {} PDB entries is ready".format(x)) 
                x += 1

print("Splitting is ready!")


## > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+pdb+'/' ## +pdb+'_'+chain+'.pdb'
"""                    
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

# In[ ]:

x = 0
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                    for i in table[table['PDB ID'] == pdb]["Res_start"].unique():
                        for j in table[table['PDB ID'] == pdb]["Res_stop"].unique():
                            #os.system('cd /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                            split_SH2D = 'pdb_selres -'+str(i)+':'+str(i)+' /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'.pdb  > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+pdb+'/'+pdb+'_'+chain+'_sH2.pdb'
                            os.system(split_SH2D)
                            #os.system('mv '+pdb+'_'+chain+'_sH2.pdb /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                            if x%1 == 0:
                                print("Already slpitted for SH2 domain {} PDB entries".format(x))
                            x += 1

print("Splitting into the SH2 domains is ready")
"""
"""

"""
table.head()


# In[ ]:


split_SH2D = 'python /home/takacsg/anaconda3/bin/pdb_selres.py -20:100 /home/takacsg/Documents/SH2DB/Structures/SigRed/3BP2/2CR4/2CR4_A.pdb  > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/2CR4_A_SH2.pdb'
os.system(split_SH2D)


# In[ ]:


os.system('pdb_selres pdb_selres -20:100 /home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A.pdb > home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A_SH2.pdb')
"""

