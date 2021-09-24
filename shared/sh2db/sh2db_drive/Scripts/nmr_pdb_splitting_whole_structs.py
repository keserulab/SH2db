import pandas as pd
from Bio import PDB
import os

pfam = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_with_pdb_nums_domcol.csv')
print(pfam.head())

# pdb_splitmodel usage in TERMINAL: pdb_splitmodel 1AB2_A.pdb
# its output 1AB2_A.pdb with just the first NMR model (last line is TER)

parser = PDB.PDBParser(QUIET=True)
x = 0
for cat in pfam["Category"].unique():
    for gene in pfam[pfam["Category"] == cat]["Gene name"].unique():
        for pdb in pfam[pfam["Gene name"] == gene]["PDB ID"].unique():
            for chain in pfam[pfam["PDB ID"] == pdb]["PDB chain ID"].unique():
                for pole in pfam[(pfam["PDB ID"] == pdb) & (pfam["PDB chain ID"] == chain)]["Pole"].unique():
                    pdb_id = str(pdb)
                    structure = parser.get_structure(pdb_id, '/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb')
                    structure = structure[0]
                    if x%1 == 0:
                        print("Already splitted {} PDB entries".format(x))
                    x += 1

print("FILE SPLITTING IS READY.")
# sed -n "1,/${SEARCHSTRING}/p" infile