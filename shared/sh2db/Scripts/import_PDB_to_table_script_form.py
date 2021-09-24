import pandas as pd

from Bio import PDB

# 3->1-betűs aminosav-kód konverzió dictionary
#from Bio.Data.IUPACData import protein_letters_3tol
from Bio.SeqUtils import seq1

pfam = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_with_pdb_nums_domcol.csv')
pfam.head()

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/proba.csv', index_col = [0,1])
table.head()

parser = PDB.PDBParser(QUIET=True)

protein_letters_3to1 = {'Ala': 'A',
 'Cys': 'C',
 'Asp': 'D',
 'Glu': 'E',
 'Phe': 'F',
 'Gly': 'G',
 'His': 'H',
 'Ile': 'I',
 'Lys': 'K',
 'Leu': 'L',
 'Met': 'M',
 'Asn': 'N',
 'Pro': 'P',
 'Gln': 'Q',
 'Arg': 'R',
 'Ser': 'S',
 'Thr': 'T',
 'Val': 'V',
 'Trp': 'W',
 'Tyr': 'Y'}

parser = PDB.PDBParser(QUIET=True)

for cat in pfam["Category"].unique():
    for gene in pfam[pfam["Category"] == cat]["Gene name"].unique():
        for pdb in pfam[pfam["Gene name"] == gene]["PDB ID"].unique():
            for chain in pfam[pfam["PDB ID"] == pdb]["PDB chain ID"].unique():
                for pole in pfam[(pfam["PDB ID"] == pdb) & (pfam["PDB chain ID"] == chain)]["Pole"].unique():
                    pdb_id = str(pdb+'_'+chain+'_SH2_'+pole)
                    try:
                        #print(pdb_id)
                        structure = parser.get_structure(pdb_id, '/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1_'+chain+'_SH2_'+pole+'_2.pdb') # struct delles pdb-fájlokat nem szereti!
                    except ValueError:
                        continue
                    #model = structure[0]
                    residues = PDB.Selection.unfold_entities(structure, "R")
                    chain = pdb_id.split('_')[1]
                    print("RESIDUES", residues)
                    for residue in residues:
                        if residue in ['Hoh']: #This can be expanded if multiple problematic residues occur
                            residues.remove(residue) # dropping key in the next line (for "Hoh")
                    print(residues)
                    #try:
                    pdbseq = list(zip([protein_letters_3to1[i.get_resname().title()] for i in residues],[i.get_id()[1] for i in residues]))
                    #except KeyError: #Hoh caused the Keyerror problem but was hard to remove
                    #    continue
                    print("PDB ID", pdb_id, "\n", "CHAIN", chain, "\n", "PDBSEQ", pdbseq)
                    increment = pfam[(pfam['PDB ID']==pdb) & (pfam["Pole"] == pole) & (pfam['PDB chain ID']==chain)]['New_uniprot_stop'].astype(int) - pfam[(pfam['PDB ID']==pdb) & (pfam["Pole"] == pole) & (pfam['PDB chain ID']==chain)]['New_PDB_stop'].astype(int)
                    # <- idáig jó - inentől nem -->
                    print("INCREMENT", increment)
                    for (resname,resid) in pdbseq:
                        try:
                            s=table.loc[(gene ,'nums')]==str(resid+increment.values[0])
                            print("S", s)
                            col=s[s].index[0]
                            print("COL", col)
                            print("GENE", gene)
                            print("PDB ID", pdb_id)
                            table.loc[(gene, pdb_id),col]=resname
                        except KeyError:
                            continue

table.to_csv('../data/table_from_alignment_with_pdbs.csv')