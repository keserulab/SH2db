import os

ids = []
uniprot_ids = open('/home/takacsg/Documents/sh2db/data/uniprot_ids_for_missing_structs.txt')
for line in uniprot_ids:
    lines = line.rstrip()
    ids.append(lines)

for ID in ids:
    print(ID) 
    get_fasta = 'wget https://www.uniprot.org/uniprot/'+ID+'.fasta'
    os.system(get_fasta)
    os.system('mv '+ID+'.fasta /home/takacsg/Documents/sh2db/FASTA')
