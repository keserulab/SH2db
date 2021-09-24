import pandas as pd
import sys
import os

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_struct.csv', engine ='python')
print(table.head())

print("TABLE FILLING HAS FINISHED")
#/home/takacsg/Documents/sh2db/Structures/Adaptors/CRK/1JU5/1JU5.pdb

x = 0
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                get_fasta = ('pdb_tofasta /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2.pdb > /home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2.fasta')
                os.system(get_fasta)
                if x%1 == 0:
                    print("Ready {} fasta files from PDB files".format(x))
                x += 1

print('DONE WITH CREATING FASTA FILES FROM PDB FILES.')