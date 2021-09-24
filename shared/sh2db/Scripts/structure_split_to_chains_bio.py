#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import Bio
from Bio import PDB
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBList
from Bio.PDB import PDBIO

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_with_pdb_nums_domcol.csv')
print(table.head())

print("TABLE READING HAS FINISHED")

#class ChainSelect(Select):
def accept_chain(self, chain):
    if chain.get_name() == chain:
        return True
    else: return False

#QUIET=True

parser = PDB.PDBParser()
io = PDBIO
x = 0
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                pdb_id = str(pdb)
                print("PDB ID: ", pdb_id)
                path_to_pdb = '/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb'
                struct = parser.get_structure(pdb_id, path_to_pdb)
                print("STRUCTURE 1: ", struct)
                #struct = struct[0]
                #print("STRUCTURE 2: ", struct)
                io.set_structure(struct)
                io.save(pdb+'_'+chain+'.pdb', accept_chain(pdb, chain))
                if x%1 == 0:
                    print("Already splitted {} PDB entries".format(x))
                x += 1

print('DONE WITH SPLITTING PDB STRUCTURES TO CHAINS')