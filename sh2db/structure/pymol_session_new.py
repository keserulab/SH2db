import __main__
__main__.pymol_argv = [ 'pymol', '-qc']
import pymol

import sys
import os

from io import BytesIO

def split_residue_lists(residues, n):
    if n==0:
        return
    else:
        for i in range(0, len(residues), n):
            yield residues[i:i+n]

outfilename = sys.argv[1]
structure_domains = sys.argv[2].strip("']['").split("', '")
#residues = sys.argv[3].strip("']['").split("', '")
residues = sys.argv[3].split(",")

length = len(residues) / len(structure_domains)
## FOR DEBUGGING
#print(structure_domains)
#print(sys.argv[3])
#print(residues)

pymol.finish_launching()

if not sys.argv[3]:
    for structure_domain in structure_domains:
        pymol.cmd.load(structure_domain, structure_domain.strip('.pdb') )
else:
    for structure_domain, resids in zip(structure_domains, split_residue_lists(residues, int(length) ) ):
        ## FOR DEBUGGING
        #print(residues)
        #print(structure_domain)
        #print(resids)
        #print(structure_domain.strip('.pdb')+' and resi '+'+'.join( [str(i) for i in resids if i] ))
        pymol.cmd.load(structure_domain, structure_domain.strip('.pdb') )
        pymol.cmd.select('s_'+structure_domain.strip('.pdb'), structure_domain.strip('.pdb')+' and resi '+'+'.join( [str(i) for i in resids if i] ))
        pymol.cmd.show('sticks', 's_'+structure_domain.strip('.pdb') )
        #pymol.cmd.show('sticks', structure_domain.strip('.pdb')+' and resi '+'+'.join( [i for i in resids if i] ) )

pymol.cmd.show('cartoon')
pymol.cmd.hide('lines')

pymol.cmd.save(outfilename)

## FOR DEBUGGING
#print(structure_domains)
#print(residues)
#print('+'.join(resids) )