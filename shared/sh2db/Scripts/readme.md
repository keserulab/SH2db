There are two main groups of scripts: one group (Group 1.) are working on the processing of the PDB files and the another group are working the processing of the tables (Group 2.).

**Group 1.**
1. 01_folder_creating.py - Creates the folder system
2. 02_download_PDB_structures.py - Downloads the pdb files. Output: .pdb
3. 03_structure_split_to_1_struct_files.py - Split the structures at every "ENDMDL" word and saves the first part into a new file: "_1.pdb" (It is needed because of the NMR structures.)
4. 04_structure_split_to_chains.py - Splits every structure to their chains and moves these chains to their place at folder system. Output: _1_A.pdb
5. 05_chains_split_to_SH2_domain_2_domains.py - It splits out the SH" domain from the chains. Output: _A_SH2.pdb
6. 06_renumbering.ipynb - Renumbers the SH2 domain's residue numbers to fit them to the UniProt numbering. Output: _A_SH2_R.pdb
7. 07_structural_alignment.ipynb - The strucutural alignment process. Output: _SUPERPOSED.pdb files

**Group 2.**
Here are two further group for the scripts based on their process target: group A scripts are working on the processes of "Pfam_table" and Group B working on the processes of the "alignment_table".

**Group A**
1. table_processing_srcipts.ipynb - Collections of differenet table processing steps on the "pfam_table", e.g.: increaseing the SH2 domain region and recalcualting the residues numbers, or converting xlsx files to csv files, etc...

**Group B**
1. table_process_B1__table_from_master_alignment.py - Creates the "alignment_table" csv file from the master alignment fasta file.
2. table_process_B2 - Downloads the fasta files based on the proteins UniPot code from UniProt's webpage. 
3. table_process_B3_pdb_to_fasta.py - Converts the pdb file to fasta files. It is needed because the resiudes of the fasta files could aligned to the "alignment_table" more easily.
4. table_process_B4_pdb_align_to_table.py - Aligns the residues from the pdb file converted to fasta files into the "alignment_table".

