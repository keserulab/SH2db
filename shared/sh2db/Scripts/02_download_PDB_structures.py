import pandas as pd
import sys
import os


table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_struct.csv')
print(table.head())
# https://files.rcsb.org/download/1AB2.pdb
print("TABLE READING HAS FINISHED")

# ## 2. Download the structures (in PDB format)

# By pdb_fetch:

x = 0
print("Categories {}".format(",".join(table["Category"].unique())))
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[(table["Gene name"] == gene) & (table["Category"] == cat)]["PDB ID"].unique():
            fetch_pdb = 'pdb_fetch '+pdb+' > /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb &'
            os.system(fetch_pdb)
            if x%1 == 0:
                print("Already fetched {} PDB entries".format(pdb)) 
            x += 1

print("ALREADY FETCHED ALL THE PDB ENTRIES.")

# Usage in terminal: time python3 Scripts/download_PDB_structures.py 
