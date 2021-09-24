#from schrodinger.maestro import maestro
from schrodinger import structure
import schrodinger


schrodinger.structure.StructureReader('/home/agnes/Documents/STAT/Structures/Phophatases/PTN11/3TKZ/3TKZ.pdb')

"""
x = 0
print("Categories {}".format(",".join(table["Category"].unique())))
for cat in table["Category"].unique():
    print("Genes {}".format(",".join(table[table["Category"] == cat]["Gene name"].unique())))
    for gene in table[table["Category"] == cat]["Gene name"].unique():
        for pdb in table[(table["Gene name"] == gene) & (table["Category"] == cat)]["PDB ID"].unique():
	    schrodinger.structure.StructureReader('/home/agnes/Documents/STAT/Structures/'+cat+'/'+gene+'/'+pdb+'/'+pdb+'.pdb)
	    x += 1
	    print("{} structures have been loaded".format(x))
"""
