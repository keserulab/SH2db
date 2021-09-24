#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

print("succesful slicing")

# ### Creating the needed folders:
# 
# Catergory folders / folders for every pdb entry

# In[ ]:

"""
# creating the category folders
for cat in table["Category"]:
    os.system('mkdir -p /home/takacsg/Documents/SH2DB/Structures/'+cat+'/')
# -p : no error if existing, make parent directories as needed


# In[ ]:


# creating the pdb folders (inside the category folders:Gene name
for cat in table["Category"]:
    for gene in table[table["Category"] == cat]["Gene name"]:
         os.system('mkdir -p /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/')"""

"""
# In[ ]:

# 5%2=1 !!

# creating the pdb folders (inside the category folders:
x = 0
for cat in table["Category"]:
    for gene in table[table["Category"] == cat]["Gene name"]:
        for pdb in table[table["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/')
            if x%100 == 0:
                print("Already created folders {} PDB entries".format(x))
            x += 1"""
# make the folders for kinases (new folder for every PDB ID)


# ## 2. Download the structures (in PDB format)

# ## `pdb_fetch` on the table slices:

# In[7]:
"""
x = 0
for cat in first["Category"]:
    for gene in first[first["Category"] == cat]["Gene name"]:
        for pdb in first[first["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%100 == 0:
                print("Already fetched in the 1. slice {} PDB entries".format(x)) 
            x += 1


# In[7]:

x = 0
for cat in second["Category"]:
    for gene in second[second["Category"] == cat]["Gene name"]:
        for pdb in second[second["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%100 == 0:
                print("Already fetched in the 2. slice {} PDB entries".format(x)) 
            x += 1


# In[ ]:

x =0
for cat in third["Category"]:
    for gene in third[third["Category"] == cat]["Gene name"]:
        for pdb in third[third["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%100 == 0:
                print("Already fetched in the 3. slice {} PDB entries".format(x)) 
            x += 1
"""

# In[ ]:

x = 0
print("Categories {}".format(",".join(table["Category"].unique())))
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[(table["Gene name"] == gene) & (table["Category"] == cat)]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > //home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%1 == 0:
                print("Already fetched {} PDB entries".format(x)) 
            x += 1
"""

# In[ ]:

x = 0
for cat in fifth["Category"]:
    for gene in fifth[fifth["Category"] == cat]["Gene name"]:
        for pdb in fifth[fifth["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%100 == 0:
                print("Already fetched in the 5. slice {} PDB entries".format(x)) 
            x += 1


# In[ ]:

x = 0
for cat in sixth["Category"]:
    for gene in sixth[sixth["Category"] == cat]["Gene name"]:
        for pdb in sixth[sixth["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/SH2DB/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%100 == 0:
                print("Already fetched in the 6. slice {} PDB entries".format(x)) 
            x += 1


"""




"""
# ## Downloading the missing PDB entries by `pdb_fetch`
# 
# ### Tasks:
# 1. Searching for the missing entries, collect them into a list (more precisely create for them a table slies)
# 2. Create the folders for the entries by PDB IDs
# 3. Download the structures

# 344 - 353 PhosLip_second_mess 412 - 421
# 355 - 512 phosphatases 432 - 594
# 526 - 527 Scaffolds 621-622
# 528 - 529 PhosLip_second_mess 623-624 (messengers)
# 599 - 618 STAT proteins 734-760
# 622 - 631 Small_gtpases  766-775
# 619 - 620 (763 - 764) - tns2

# In[ ]:


phospholipid_messengers = pfam_table[342:352]
phosphatases = pfam_table[353:411]
phosphatases2 = pfam_table[412:511]
scaffolds = pfam_table[524:526]
messengers2 = pfam_table[524:525]
STATS = pfam_table[597:617]
small_gtpases = pfam_table[620:630]
tns = pfam_table[617:619]


# In[ ]:


#print("lipid messengers", '\n', phospholipid_messengers.head(), '\n')
#print("phosphatases", '\n', phophatases.head(), '\n')
#print("scaffolds", '\n', scaffolds.head(), '\n')
#print("messengers2", '\n', messengers2.head(), '\n')
#print("STATS", '\n', STATS.head(), '\n')
#print("Small gtpases", '\n', small_gtpases.head(), '\n')
#print("tns", '\n', tns.head(), '\n')


# In[ ]:


#print("lipid messengers", '\n', phospholipid_messengers.tail(), '\n')
#print("phosphatases", '\n', phophatases.tail(), '\n')
#print("scaffolds", '\n', scaffolds.tail(), '\n')
#print("messengers2", '\n', messengers2.tail(), '\n')
#print("STAT", '\n', STATS.tail(), '\n')
#print("small gtpases", '\n', small_gtpases.tail(), '\n')
#print("tns", '\n', tns.tail(), '\n')


# ### Phospholipid second messengers:

# In[ ]:


for cat in phospholipid_messengers["Category"]:
    for gene in phospholipid_messengers[phospholipid_messengers["Category"] == cat]["Gene name"]:
        for pdb in phospholipid_messengers[phospholipid_messengers["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


# In[ ]:


for cat in phospholipid_messengers["Category"]:
    for gene in phospholipid_messengers[phospholipid_messengers["Category"] == cat]["Gene name"]:
        for pdb in phospholipid_messengers[phospholipid_messengers["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# In[ ]:


for cat in messengers2["Category"]:
    for gene in messengers2[messengers2["Category"] == cat]["Gene name"]:
        for pdb in messengers2[messengers2["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


# In[ ]:


for cat in messengers2["Category"]:
    for gene in messengers2[messengers2["Category"] == cat]["Gene name"]:
        for pdb in messengers2[messengers2["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# ### STATs:

# In[ ]:


for cat in STATS["Category"]:
    for gene in STATS[STATS["Category"] == cat]["Gene name"]:
        for pdb in STATS[STATS["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


# In[ ]:


for cat in STATS["Category"]:
    for gene in STATS[STATS["Category"] == cat]["Gene name"]:
        for pdb in STATS[STATS["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# ### Scaffolds: 

# In[ ]:


for cat in scaffolds["Category"]:
    for gene in scaffolds[scaffolds["Category"] == cat]["Gene name"]:
        for pdb in scaffolds[scaffolds["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')
            

for cat in scaffolds["Category"]:
    for gene in scaffolds[scaffolds["Category"] == cat]["Gene name"]:
        for pdb in scaffolds[scaffolds["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# ### Phosphatases:

# In[ ]:


for cat in phosphatases["Category"]:
    for gene in phosphatases[phosphatases["Category"] == cat]["Gene name"]:
        for pdb in phosphatases[phosphatases["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


# In[ ]:


for cat in phosphatases["Category"]:
    for gene in phosphatases[phosphatases["Category"] == cat]["Gene name"]:
        for pdb in phosphatases[phosphatases["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# In[ ]:


for cat in phosphatases2["Category"]:
    for gene in phosphatases2[phosphatases2["Category"] == cat]["Gene name"]:
        for pdb in phosphatases2[phosphatases2["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


# In[ ]:


for cat in phosphatases2["Category"]:
    for gene in phosphatases2[phosphatases2["Category"] == cat]["Gene name"]:
        for pdb in phosphatases2[phosphatases2["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# ###  Small GTPases:

# In[ ]:


for cat in small_gtpases["Category"]:
    for gene in small_gtpases[small_gtpases["Category"] == cat]["Gene name"]:
        for pdb in small_gtpases[small_gtpases["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')            


# In[ ]:


for cat in small_gtpases["Category"]:
    for gene in small_gtpases[small_gtpases["Category"] == cat]["Gene name"]:
        for pdb in small_gtpases[small_gtpases["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# ### TNS:

# In[ ]:


for cat in tns["Category"]:
    for gene in tns[tns["Category"] == cat]["Gene name"]:
        for pdb in tns[tns["Gene name"] == gene]["PDB ID"]:
            os.system('mkdir -p /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')
            

for cat in tns["Category"]:
    for gene in tns[tns["Category"] == cat]["Gene name"]:
        for pdb in tns[tns["Gene name"] == gene]["PDB ID"]:
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)


# In[ ]:





# ## 3. Split the protein into chains by pdb-tools `pdb_splitchain`
# 
# - pdb_splitchain: splits a pdb file into several, each containing one chain.
# - output file names will be: pdbid_A.pdb pdbid_B.pdb
# - usage: pdb_splitchain 2cr4.pdb

# In[ ]:


for cat in pfam_table["Category"]:
    for gene in pfam_table[pfam_table["Category"] == cat]["Gene name"]:
        for pdb in pfam_table[pfam_table["Gene name"] == gene]["PDB ID"]:
            for chain in pfam_table[pfam_table["PDB ID"] == pdb]["PDB chain ID"]:
                split_pdb = 'pdb_splitchain /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb' ## > /home/agnes/Documents/STAT/Structures/'+cat+'/'+pdb+'/' ## +pdb+'_'+chain+'.pdb'
                os.system(split_pdb)
                os.system('mv '+pdb+'_'+chain+'.pdb /home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/')


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


for cat in pfam_table["Category"]:
    for gene in pfam_table[pfam_table["Category"] == cat]["Gene name"]:
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


os.system('pdb_selres pdb_selres -20:100 /home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A.pdb > home/agnes/Documents/STAT/Structures/SigRed/3BP2/2CR4/2CR4_A_SH2.pdb')"""

