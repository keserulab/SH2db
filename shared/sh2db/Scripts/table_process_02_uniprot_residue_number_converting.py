import pandas as pd
import numpy 

table = pd.read_csv('/sh2db_vagrant/SH2db/shared/data/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv', engine ='python')
#print(table.head())

table["New_uniprot_start"] = table["New_uniprot_start"] + 1
table["New_uniprot_stop"] = table["New_uniprot_stop"] + 4

#print("Table with fixed new uniprot start/stop numbers", "\n", table.head())

# Separating the values into two new columns from the "UniProt residues" column
# # (It needed to recalcualte the PDB residue numbers for the right residue numbers) 
for i in table.index.values:
    table.loc[i, "Old_uniprot_start"] = table.loc[i, "UniProt residues"].split(' - ')[0]
    table.loc[i, "Old_uniprot_stop"] = table.loc[i, "UniProt residues"].split(' - ')[1] 

#print("Table with new cols", "\n", table.head(20))
#print("Table with new cols", "\n", table.tail(20))

# Calculating the new residue numbers for start points:

# Converting the colunm values to integers (now they are strs):
table["New_uniprot_start"] = table["New_uniprot_start"].astype(int)
table["Old_uniprot_start"] = table["Old_uniprot_start"].astype(int)
# Calculating the difference between the new and old start points:
table["diff_start"] = table["Old_uniprot_start"] - table["New_uniprot_start"]

# Get the new start point for PDB residues:
table["New_PDB_start"] = table["Res_start"] - table["diff_start"]
# Checking it's succes:
#print("New PDB residue start calculating", "\n", table.head(15))


# Calculating the new residue numbers for start points:

# Converting the colunm values to integers (now they are strs):
table["New_uniprot_stop"] = table["New_uniprot_stop"].astype(int)
table["Old_uniprot_stop"] = table["Old_uniprot_stop"].astype(int)
# Calculating the difference between the new and old stop points:
table["diff_stop"] = table["New_uniprot_stop"] - table["Old_uniprot_stop"]

# Get the new start point for PDB residues:
table["New_PDB_stop"] = table["Res_stop"] + table["diff_stop"]

# Checking it's succes:
#print("New PDB residue stop calculating", "\n", table.head(15))
#for i in table["New_PDB_stop"]:
#    i.clip(0)

table["New_PDB_stop"] = table["New_PDB_stop"].clip(0)
table["New_PDB_start"] = table["New_PDB_start"].clip(0)

table.to_csv("SH2_domain_containing_prot_right_resnum_negatives_to_zero.csv", index = False)

# After the script, it is needed to fix the residue numbers (New_uniprot_start/stop) what were added to tha table by hands.
# There, just subtract 1 from start point numbers and subtract 4 from stop points numbers (columns: New_PDB_start/stop, New_PDB_start/stop)
# Cases when it is needed: 
# where there is a second SH2-domain
# ZAP70, SYK, PLCG1, PLCG2, PTPN6, PIK3R1, PIK3R2, PIKR3R3, RASA1