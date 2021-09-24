import pandas as pd
import numpy 

table = pd.read_csv('/home/takacsg/Documents/sh2db/data/SH2_domain_containing_prot_right_resnum_fixed.csv', engine ='python')
#print(table.head())

# Calculating the new residue numbers for START points:

# Converting the colunm values to integers (now they are strs):
table["New_uniprot_start"] = table["New_uniprot_start"].astype(int)
table["Old_uniprot_start"] = table["Old_uniprot_start"].astype(int)
# Calculating the difference between the new and old start points:
table["diff_start"] = table["Old_uniprot_start"] - table["New_uniprot_start"]

# Get the new start point for PDB residues:
table["New_PDB_start"] = table["Res_start"] - table["diff_start"]
# Checking it's succes:
print("New PDB residue start calculating", "\n", table.head(15))


# Calculating the new residue numbers for STOP points:

# Converting the colunm values to integers (now they are strs):
table["New_uniprot_stop"] = table["New_uniprot_stop"].astype(int)
table["Old_uniprot_stop"] = table["Old_uniprot_stop"].astype(int)
# Calculating the difference between the new and old stop points:
table["diff_stop"] = table["New_uniprot_stop"] - table["Old_uniprot_stop"]

# Get the new start point for PDB residues:
table["New_PDB_stop"] = table["Res_stop"] + table["diff_stop"]

# Checking it's succes:
print("New PDB residue stop calculating", "\n", table.head(15))

table["New_PDB_stop"] = table["New_PDB_stop"].clip(0)
table["New_PDB_start"] = table["New_PDB_start"].clip(0)

table.to_csv("../data/SH2_domain_containing_prot_right_resnum_with_pdb_nums.csv")
