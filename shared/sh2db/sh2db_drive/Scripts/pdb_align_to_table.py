import sys
import pandas as pd
import argparse
import logging

"""
Recommended usage:
cat ../data/table_from_alignment.csv | python3 pdb_align_to_table.py ../data/SH2_domain_containing_prot_right_resnum_fixed.csv > table_from_alignment_extended2.csv
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
print(table.head())

fasta_dict = {}
#line_lst = []
for cat in table["Category"].unique():
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[table["Gene name"] == gene]["PDB ID"].unique():
            for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                for chain in table[table["PDB ID"] == pdb]["PDB chain ID"].unique():
                    with open('/home/takacsg/Documents/sh2db/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'_'+chain+'_SH2.fasta', 'r') as fasta:
                        for line in fasta:
                            logger.info(line)
                            if line[0] == '>':
                                logger.info("Found fasta: %s", line)
                                line_lst = []
                                continue
                            else:
                                line = line.rstrip()
                                line_lst.append(line)
                        fasta_dict[pdb] = ''.join(line_lst)
                        logger.info("Current pdb: %s", fasta_dict[pdb])

gene_name_dict = {}
for gene_name in table["Gene name"].unique():
    gene_name_dict[gene_name] = []
    for pdb_id in table[table["Gene name"] == gene_name]["PDB ID"].unique():
        gene_name_dict[gene_name].append(pdb_id)


for sh2_csv_line in sys.stdin:
    sh2_csv_list = sh2_csv_line.rstrip().split(',')
    print(sh2_csv_line)
    try:
        pdb_id_list = gene_name_dict[sh2_csv_list[0]]
    except KeyError: 
        pdb_id_list = []
    for x in pdb_id_list:
        print(','+x+','+ ','.join(fasta_dict[x]))    # ','+x -> x should be in the 2. column:


