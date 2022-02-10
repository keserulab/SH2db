from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from common.models import Publication, WebLink, WebResource, Journal
from protein.models import Domain, Sequence
from structure.models import Structure, Chain, StructureDomain, PDBData, StructureType

import csv
import os
import pprint
import urllib
import json
from datetime import datetime


class Command(BaseBuild):

    pdbs = []
    chains = {}
    domains = {}
    pdbs_path = os.sep.join([settings.DATA_DIR, 'structures'])

    def add_arguments(self, parser):
        parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        parser.add_argument("--purge", default=False, action="store_true", help="Purge data")

    def handle(self, *args, **options):
        if options['purge']:
            PDBData.objects.all().delete()
            Domain.objects.filter(parent__isnull=False).delete()
            Publication.objects.all().delete()
            StructureDomain.objects.all().delete()
            Chain.objects.all().delete()
            Structure.objects.all().delete()
            StructureType.objects.all().delete()

        self.parse_alignment_file()
        
        # Structures
        self.build_structure_objects()

        # Chains
        self.build_chains()

        # Domains
        self.build_structure_domains()

    def parse_alignment_file(self):
        with open(os.sep.join([settings.DATA_DIR, 'table_from_alignment_with_pdbs_0917.csv']), newline='') as csvfile:
            structure_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(structure_reader):
                # PDB IDs
                if row[1]!='nums' and row[1]!='seq' and len(row[1])>3:
                    pdb = row[1][:4]
                    chain = row[1][5]
                    domain = row[1][-1]
                    gene = row[0].split('_')[0]
                    seq = ''.join(row[2:]).replace('-','')
                    if pdb not in self.pdbs:
                        self.pdbs.append(pdb)
                        self.chains[pdb] = [chain]
                        self.domains[pdb] = {'chains':{chain:[domain, seq]}, 'gene':gene}
                    else:
                        if chain not in self.chains[pdb]:
                            self.chains[pdb].append(chain)
                        if chain not in self.domains[pdb]['chains']:
                            self.domains[pdb]['chains'][chain] = [domain, seq]

    def build_pdbdata(self, filename):
        with open(filename, 'r') as f:
            pdbdata = f.read()
        pdbdata, created = PDBData.objects.get_or_create(pdb=pdbdata)
        return pdbdata

    def build_structure_domains(self):
        for pdb, vals in self.domains.items():
            for chain, domain in vals['chains'].items():
                try:
                    chain_obj = Chain.objects.get(structure__pdb_code=pdb, chain_ID=chain)
                except Chain.DoesNotExist:
                    continue
                parent_domain = Domain.objects.get(isoform__protein__name=vals['gene'], domain_type__slug=domain[0], parent__isnull=True)
                seq, created = Sequence.objects.get_or_create(sequence=domain[1])
                # Protein domain
                prot_domain, created = Domain.objects.get_or_create(isoform=parent_domain.isoform, domain_type=parent_domain.domain_type, sequence=seq, parent=parent_domain)
                # PDBData
                pdbdata = self.build_pdbdata(os.sep.join([self.pdbs_path, parent_domain.isoform.protein.family.name.replace(' ','_'), parent_domain.isoform.protein.name, pdb, '{}_{}_SH2_{}_SUPERPOSED.pdb'.format(pdb,chain,domain[0])]))
                # Structure domain
                struct_domain, created = StructureDomain.objects.get_or_create(chain=chain_obj, domain=prot_domain, pdbdata=pdbdata)


    def build_chains(self):
        for pdb, chain_IDs in self.chains.items():
            for chain_ID in chain_IDs:
                try:
                    structure = Structure.objects.get(pdb_code=pdb)
                except Structure.DoesNotExist:
                    continue
                chain, created = Chain.objects.get_or_create(chain_ID=chain_ID, structure=Structure.objects.get(pdb_code=pdb))

    def build_structure_objects(self):
        for pdb in self.pdbs:
            data = self.pdb_request_by_pdb(pdb)
            if len(data)==0:
                continue

            # Structure type
            method = self.build_structure_type(data['method'])

            # Publication
            pub = self.build_publication(data)

            # Structure
            structure, created = Structure.objects.get_or_create(pdb_code=pdb, publication_date=data['publication_date'], publication=pub, 
                                                                 resolution=data['resolution'], structure_type=method)

    def build_structure_type(self, method):
        if method=='SOLUTION NMR':
            method, created = StructureType.objects.get_or_create(slug='NMR', name='Solution NMR')
        elif method=='X-RAY DIFFRACTION':
            method, created = StructureType.objects.get_or_create(slug='X-ray', name='X-ray diffraction')
        else:
            print('Warning: new method type ', data['method'])
            method = None
        return method

    def build_publication(self, data):
        journal, created = Journal.objects.get_or_create(name=data['journal'])
        if data['doi']:
            doi, created = WebLink.objects.get_or_create(index=data['doi'], web_resource=WebResource.objects.get(slug='doi'))
        else:
            doi = None
        pub, created = Publication.objects.get_or_create(journal=journal, title=data['title'], authors=data['authors'], year=data['year'], reference=doi)
        return pub

    def pdb_request_by_pdb(self, pdb):
        data = {}
        try:
            response = urllib.request.urlopen('https://data.rcsb.org/rest/v1/core/entry/{}'.format(pdb))
        except urllib.error.HTTPError:
            print('Error: {} PDB ID not found on RCSB.')
            return data
        json_data = json.loads(response.read())
        response.close()
        # pprint.pprint(json_data)
        data['method'] = json_data['exptl'][0]['method']
        data['journal'] = json_data['citation'][0]['rcsb_journal_abbrev']
        if 'pdbx_database_id_doi' in json_data['citation'][0]:
            data['doi'] = json_data['citation'][0]['pdbx_database_id_doi']
        else:
            data['doi'] = None
        data['authors'] = json_data['citation'][0]['rcsb_authors']
        data['title'] = json_data['citation'][0]['title']
        if 'year' in json_data['citation'][0]:
            data['year'] = json_data['citation'][0]['year']
        else:
            data['year'] = None
        if 'resolution_combined' in json_data['rcsb_entry_info']:
            data['resolution'] = json_data['rcsb_entry_info']['resolution_combined'][0]
        else:
            data['resolution'] = None
        data['publication_date'] = json_data['rcsb_accession_info']['initial_release_date'][:10]
        return data
