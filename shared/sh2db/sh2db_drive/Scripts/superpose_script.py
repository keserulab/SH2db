import pandas as pd
import Bio.PDB
from Bio import PDB


basedir = "~/SH2_vagrant/shared/sh2db_drive/"

pfam = pd.read_csv(basedir+'data/SH2_domain_containing_prot_right_resnum_with_pdb_nums_domcol_0503.csv')
pfam.drop(['Unnamed: 0'], 'columns', inplace = True)

length = pfam['New_uniprot_stop'] - pfam['New_uniprot_start']
type(length)
length.idxmax()

table = pd.read_csv(basedir+'/table_from_alignment_with_pdbs_0705_JO.csv', index_col = [1,2])
table = table.fillna('')
table.drop(['Unnamed: 0'], 'columns', inplace = True)



parser = PDB.PDBParser(QUIET=True)


target_structure = parser.get_structure('1BF5_A_SH2_C', basedir+'Structures/Transcription/STAT1/1BF5/1BF5_1_A_SH2_C_R.pdb')
target_model = target_structure[0]
target_residues = PDB.Selection.unfold_entities(target_model, "R")
print('STAT5B_residues', target_residues)

for cat in pfam["Category"].unique():
    for gene in pfam[pfam["Category"] == cat]["Gene name"].unique():
        for pdb in pfam[pfam["Gene name"] == gene]["PDB ID"].unique():
            for chain in pfam[pfam["PDB ID"] == pdb]["PDB chain ID"].unique():
                for pole in pfam[(pfam["PDB ID"] == pdb) & (pfam["PDB chain ID"] == chain)]["Pole"].unique():
                    
                    # 0. Create a variable for identifying the pdb files
                    pdb_id = str(pdb+'_'+chain+'_SH2_'+pole)
                    print(pdb_id)
                    
                    
                    # 1. 2 pdb to compare them
                    target = table.loc[('STAT1' , '1BF5_A_SH2_C')]
                    query = table.loc[(gene ,pdb_id)]
                    #print("Q", query)
                    #print("T", target)
                    
                    
                    # 2. Take the cells where there is something different than: '','-',' ' 
                    # Target is the sequence what will be used as a template in the alignment - STAT5B
                    target_indices=[idxi for (idxi,i) in zip(query.keys(),query.values) if i not in ['','-',' ']]
                    # Query is the structure what will be aligned to the target structure
                    query_indices=[idxi for (idxi,i) in zip(target.keys(),target.values) if i not in ['','-',' ']]
                    
                    
                    # 3. take the intersection of the two lists
                    common_indices = [i for i in target_indices if i in query_indices]
                    #print("common_indices", common_indices)

                    
                    # 4. Searching for the residue numbers and create two lists for the structure alignment input
                    target_seq = table.loc[('STAT1','nums')][common_indices].values
                    query_seq = table.loc[(gene,'nums')][common_indices].values
                    print("len target", len(target_seq))
                    print("len query", len(query_seq))
                    print("target_seq", target_seq)
                    print("query_seq", query_seq)
                    
                    
                    # 5. Load the PDB structures:
                    
                    query_structure = parser.get_structure(pdb_id, basedir+'Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1_'+chain+'_SH2_'+pole+'_R.pdb')
                    query_model = query_structure[0]
                    print('Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1_'+chain+'_SH2_'+pole+'.pdb')

                    query_residues = PDB.Selection.unfold_entities(query_model, "R")
                    print('query_residues', query_residues)
                                        
                    # 6. get the list of the atoms from the loaded stucture:
                    
                    target_atoms = []                    
                    # Iterate all in the STAT5B model to find all residues
                    for target_chain in target_model:
                        for target_res in target_chain:
                            print("target RES", "\n", target_res)
                            print("target get id", target_res.get_id())
                            # If the STAT5B residue is in the query_seq add it to the STAT5B atoms list
                            if str(target_res.get_id()[1]) in target_seq:
                                print("STAT5B get id", target_res.get_id())
                                target_atoms.append(target_res['CA'])
                    
                    query_atoms = []                    
                    for query_chain in query_model:
                        for query_res in query_chain:
                            print("QUERY RES", "\n", query_res)
                            print("query get id", query_res.get_id()) 
                            if str(query_res.get_id()[1]) in query_seq: # str() nélkül is dob egy out of range error-t :(
                                print("query get id", query_res.get_id())
                                query_atoms.append(query_res['CA'])

                    print(target_seq)
                    print(query_seq)             
                    print(len(target_atoms))
                    print(len(query_atoms))
                    
                    # Superimpose the structures:
                    
                    # Specify the atom lists
                    # 'query_seq' and 'target_seq' are lists of Atom objects
                    # The target_seq atoms will be put on the query_seq
                    super_imposer = Bio.PDB.Superimposer()
                    super_imposer.set_atoms(target_atoms, query_atoms)
                    
                    # Apply rotation/translation to the target_seq atoms
                    super_imposer.apply(query_structure.get_atoms())
                    # Print rotation/translation & RMSD
                    print(super_imposer.rotran)
                    print(super_imposer.rms)
                    # Save the aligned structure
                    io = PDB.PDBIO()
                    io.set_structure(query_structure)
                    io.save( basedir+'Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_1_'+chain+'_SH2_'+pole+'_2_SUPERPOSED.pdb') # MAPPA!!