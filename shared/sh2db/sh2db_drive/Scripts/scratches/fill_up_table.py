import pandas as pd

table = pd.read_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop.csv')
print(table.head())

table.fillna(method='ffill', inplace = True)
print(table.head(25))

table.to_csv('/home/takacsg/Documents/SH2DB/SH2_domain_containing_prot_new_uniprot_start_stop_filled.csv')
