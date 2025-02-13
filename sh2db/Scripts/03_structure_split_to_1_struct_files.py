#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
"""from Bio import PDB
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBList
from Bio.PDB import PDBIO"""

def ter_splitter(path_to_pdb):
    path_to_pdb_splitted = str(path_to_pdb.split(".")[0] + "_1.pdb")
    with open(path_to_pdb, "r") as infile:
        with open(path_to_pdb_splitted, "w") as outfile:
            for line in infile:
                outfile.write(line)
                linestart = line[:6]
                #print(linestart)
                if linestart == "ENDMDL":
                    return path_to_pdb_splitted
    return path_to_pdb_splitted




table = pd.read_csv('/sh2db_vagrant/SH2db/shared/data/pfam_table_recalculated_0830.csv')
print(table.head())

print("TABLE READING HAS FINISHED")

#parser = PDB.PDBParser()
#io = PDBIO

x = 0
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                pdb_id = str(pdb)
                print("PDB ID: ", pdb_id)
                path_to_pdb = '/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb'
                path_to_pdb_splitted = ter_splitter(path_to_pdb)

                #struct = parser.get_structure(pdb_id, path_to_pdb_splitted)
                #print("STRUCTURE 1: ", struct)
                #struct = struct[0]
                #print("STRUCTURE 2: ", struct)
                #io.set_structure(struct)
                #io.save(pdb+'_'+chain+'.pdb', accept_chain(pdb, chain))
                if x%1 == 0:
                    print("Already splitted {} PDB entries".format(x))
                x += 1

print('DONE WITH SPLITTING PDB STRUCTURES TO CHAINS')
