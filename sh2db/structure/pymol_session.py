import __main__
__main__.pymol_argv = [ 'pymol', '-qc']
import pymol

import sys
import os

from io import BytesIO

outfilename = sys.argv[1]
structure_domains = sys.argv[2].strip("']['").split("', '")
residues = sys.argv[3].strip("']['").split("', '")

resids = [ i[1:] for i in residues]

pymol.finish_launching()
for structure_domain in structure_domains:
    pymol.cmd.load(structure_domain, structure_domain.strip('.pdb') )
    pymol.cmd.show('sticks', structure_domain.strip('.pdb')+' and resi '+'+'.join(resids) )

pymol.cmd.show('cartoon')
pymol.cmd.hide('lines')

pymol.cmd.save(outfilename)

## FOR DEBUGGING
#print(structure_domains)
#print(residues)
#print('+'.join(resids) )