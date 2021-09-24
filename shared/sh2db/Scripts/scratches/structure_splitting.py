#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio.PDB import PDBList
import sys
import os

table = pd.read_excel('/home/takacsg/Documents/SH2DB/filtered_table_with_uniprot_ids.xlsx')
print(table.head())

print("succesful read in")

# In[3]:

"""
table.fillna(method='ffill', inplace = True)
table.head()
"""

print("succesful fill in")

# ## Split into more table the pfam_table:

# In[6]:

"""
#first = table[:10]
#second = table[10:20]
#third = table[20:30]
fourth = table[30:50]

fifth = table[400:500]
sixth = table[500:]"""

#print("succesful slicing")

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
                split_pdb = 'python /home/takacsg/anaconda3/lib/python3.8/site-packages/pdbtools/pdb_splitchain /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb' 
                os.system(split_pdb)
                os.system('mv '+pdb+'_'+chain+'.pdb /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                if x%1 == 0:
                    print("Already splitted {} PDB entries".format(x)) 
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

# In[ ]:

"""
for cat in pfam_table["Category"]:
    for gene in pfam_table[pfam_table["Category"] == cat]["Gene name"].unique():
        for pdb in pfam_table[pfam_table["Gene name"] == gene]["PDB ID"]:
            for chain in pfam_table[pfam_table["PDB ID"] == pdb]["PDB chain ID"]:
                for chain in pfam_table[pfam_table["PDB ID"] == pdb]["PDB chain ID"]:
                    for i in pfam_table[pfam_table['PDB ID'] == pdb]["Res_start"]:
                        for j in pfam_table[pfam_table['PDB ID'] == pdb]["Res_stop"]:
                            #os.system('cd /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                            split_SH2D = 'python pdb_selres.py -'+i+':'+j+' /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'.pdb  > /home/agnes/Documents/STAT/Structures/'+cat+'/'+pdb+'/'+pdb+'_'+chain+'_sH2.pdb'
                            os.system(split_SH2D)
                            os.system('mv '+pdb+'_'+chain+'_sH2.pdb /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


# In[ ]:


pfam_table.head()


# In[ ]:


split_SH2D = 'pdb_selres -20:100 /home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A.pdb  > /home/agnes/Documents/STAT/Structures/'+cat+'/'+pdb+'/'+pdb+'_'+chain+'_sH2.pdb'
os.system(split_SH2D)


# In[ ]:


os.system('pdb_selres pdb_selres -20:100 /home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A.pdb > home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A_SH2.pdb')
"""

