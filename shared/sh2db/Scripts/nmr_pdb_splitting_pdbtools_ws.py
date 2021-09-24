import pandas as pd
import sys
import os

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_with_pdb_nums_domcol.csv')
print(table.head())

# pdb_splitmodel usage in TERMINAL: pdb_splitmodel 1AB2_A.pdb
# its output 1AB2_A.pdb with just the first NMR model (last line is TER)


for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
                split_files = 'pdb_splitmodel /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb'
                os.system(split_files)
                os.system('mv '+pdb+'.pdb /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                print(pdb)

print("FILE SPLITTING IS READY.")