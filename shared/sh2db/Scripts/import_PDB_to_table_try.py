import pandas as pd

from Bio import PDB

# 3->1-betűs aminosav-kód konverzió dictionary
from Bio.Data.IUPACData import protein_letters_3to1

pfam = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_fixed.csv')
pfam.head()

# Read in the alignment table:
table=pd.read_csv('/home/takacsg/Documents/sh2db/data/table_alignment.csv',index_col=[0,1])

# PDB beolvasása, residues a residuek listája
for cat in pfam["Category"].unique():
    for gene in pfam[pfam["Category"] == cat]["Gene name"].unique():
        for pdb in pfam[pfam["Gene name"] == gene]["PDB ID"].unique():
            for chain in pfam[pfam["PDB ID"] == pdb]["PDB chain ID"].unique():
                with open('/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2.pdb') as struct:
                    parser = PDB.PDBParser()
                    pdb_id = str(pdb+'_'+chain+'_SH2')
                        #file =str(pdb+'_'+chain+'_SH2.pdb')
                    structure = parser.get_structure(pdb_id, struct) # Sok-modelles pdb-fájlokat nem szereti!
                    #model = structure[0]
                    residues = PDB.Selection.unfold_entities(structure, "R")
                    # get the chain IDs
                    chain=+pdb+'_'+chain+'_SH2'.split('_')[1]
                    # Take out the one letter code of the amino acids with the residue numbers 
                    pdbseq=list(zip([protein_letters_3to1[i.get_resname().title()] for i in residues],[i.get_id()[1] for i in residues]))

# Calculating the difference between the new uniprot stop and new pdb stop points:
for cat in pfam["Category"].unique():
    for gene in pfam[pfam["Category"] == cat]["Gene name"].unique():
        for pdb in pfam[pfam["Gene name"] == gene]["PDB ID"].unique():
            increment = int(pfam[pfam['PDB ID']==pdb]['New_uniprot_stop'] - pfam[pfam['PDB ID']==pdb]['New_PDB_stop'])

for (resname,resid) in pdbseq:
    s=table.loc[(gene ,'numbers')]==str(resid+increment)
    col=s[s].index[0]
    #eddig ugyanaz mint fentebb, csak az oszlopindexet mentjük a col változóba
    
    table.loc[('SH3BP2','2CR4_A'),col]=resname
    # ezzel pedig beírtuk resname-et a megfelelő helyre