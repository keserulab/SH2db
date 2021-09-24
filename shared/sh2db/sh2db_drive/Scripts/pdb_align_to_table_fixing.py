import sys
import pandas as pd
import argparse
import logging

"""
Recommended usage:
cat ../data/table_from_alignment.csv | python3 pdb_align_to_table.py ../data/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv > table_from_alignment_extended.csv
"""

parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter
        )
parser.add_argument(
    type=str, 
    dest='protein_table_input'
    )
args = parser.parse_args()

#Logging setup by TG
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


protein_table_input = args.protein_table_input

table = pd.read_csv(protein_table_input, engine ='python', header=0)
#table["PDB ID"] = table["PDB ID"].astype('str')
#print(table.head())

fasta_dict = {}
#line_lst = []
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            fasta_dict[pdb] = {}
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                # Iterating over the 'table' then open the given pdb entry's fasta file.
                with open('/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2.fasta', 'r') as fasta:
                    for line in fasta:
                        logger.info(line)
                        if line[0] == '>':
                            logger.info("Found fasta: %s", line) # line e.g. >PDB|C
                            line_lst = [] # line_lst list stay empty here, it will contain the sequences (the lines in the fasta file refer to the sequence)
                            continue
                        else:
                            line = line.rstrip() # strip down the new line characters from the end of the rows -> the sequences should be one line
                            line_lst.append(line) # Appending the line_lst list with the sequence from the opened fasta file
                    fasta_dict[pdb][chain] = ''.join(line_lst) # Uploading the "fast_dict" with the PDB ID and the corresponding sequence
                    logger.info("Current pdb: %s", fasta_dict[pdb]) # fasta_dict[pdb] = Current pdb: LIIGFISKQYVTSLLLNEPDGTFLLRFSDSEIGGITIAHVIRGGSPQIENIQPFSAKDLSIRSLGDRIRDLAQLKNLY

# fasta_dict: keys: PDB IDs, values: sequence from the given PDB entry's fasta file

print("fasta dict ", fasta_dict)

gene_name_dict = {}
for gene_name in table["Gene name"].unique():
    gene_name_dict[gene_name] = []
    for pdb_id in table[table["Gene name"] == gene_name]["PDB ID"].unique():
        gene_name_dict[gene_name].append(pdb_id)

print("gene name dict ", gene_name_dict)            
# Upload the dictionary when there is a connection between Gene name and the PDB ID based on the table(SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv)
# std in: table_from_alignment

for sh2_csv_line in sys.stdin:
    sh2_csv_list = sh2_csv_line.rstrip().split(',')
    print("LINE", sh2_csv_line)
    try:
        # gene_name_dict[sh2_csv_list[0]]: pdb_id_list-be tárolni azt amikor a gene_name_dict key == sh2_csv_list
        pdb_id_list = gene_name_dict[sh2_csv_list[0]]
        logger.info("pdb id list: %s", pdb_id_list)
        #print("pdb id list", pdb_id_list)
    except KeyError:
        #print() 
        pdb_id_list = {}

    for pdb_id in pdb_id_list:
        logger.info("Found pdb id in in pdb_id_list: %s", pdb_id)
        # for chain in pdb_id:
        #x = str(pdb_id + ' ' + chain)
        for chain in fasta_dict[pdb_id].keys():
            #x = fasta_dict[pdb_id].keys()
            x = str(pdb_id+'_'+chain)
            logger.info('pdb id: %s, chain: %s',pdb_id, chain)
            print(','+x+','+','.join(fasta_dict[pdb_id][chain]))    # ','+x -> x should be in the 2. column


