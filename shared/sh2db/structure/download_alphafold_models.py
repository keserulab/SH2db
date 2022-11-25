from urllib.request import urlopen

with open('../data/protein_data.csv', 'r') as f:
    lines = f.readlines()

for line in lines:
    fam, gene, species, accession = line.rstrip('\n').split(',')
    url = 'https://alphafold.ebi.ac.uk/files/AF-{}-F1-model_v3.pdb'.format(accession)
    pdbdata_raw = urlopen(url).read().decode('utf-8')
    with open('../data/models/{}.pdb'.format(accession), 'w') as f:
        f.write(pdbdata_raw)
