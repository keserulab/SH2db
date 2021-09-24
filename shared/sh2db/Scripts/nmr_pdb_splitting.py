import pandas as pd
import sys
import os

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_struct.csv')
print(table.head())

# pdb_splitmodel usage in TERMINAL: pdb_splitmodel 1AB2_A.pdb
# its output 1AB2_A.pdb with just the first NMR model (last line is TER)


x = 0
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                split_files = 'pdb_splitmodel /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'.pdb'
                os.system(split_files)
                #os.system('mv '+pdb+'_'+chain+'.pdb /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/')
                if x%1 == 0:
                    print("Already splitted {} PDB entries".format(x))
                x += 1

print("FILE SPLITTING IS READY.")