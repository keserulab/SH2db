from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from protein.models import Protein, ProteinConformation, ProteinState, Species, ProteinFamily, Isoform, Sequence, DomainType, Domain

import csv
import os
import pprint


class Command(BaseBuild):

    species_latin = {'HUMAN':'Homo sapiens'}
    families = []
    proteins = {}
    species = []
    fam_objects = {}
    species_objects = {}
    protein_seqs = {}

    def add_arguments(self, parser):
        parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        parser.add_argument("--purge", default=False, action="store_true", help="Purge data")

    def handle(self, *args, **options):
        if options['purge']:
            Protein.objects.all().delete()
            ProteinFamily.objects.all().delete()
            Species.objects.all().delete()

        # parsing data file
        self.parse_file()
        with open(os.sep.join([settings.DATA_DIR, 'domains_without_structure_1119.csv']), newline='') as csvfile:
            uniprot_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for i, row in enumerate(uniprot_reader):
                if i==0:
                    continue
                self.proteins[row[2]] = ['',row[1],'HUMAN',row[3]]
        pprint.pprint(self.proteins)
        with open(os.sep.join([settings.DATA_DIR, 'protein_data.csv']), 'w') as f:
            for i, j in self.proteins.items():
                f.write(','.join(j)+'\n')
        return 0
        # creating families
        self.build_families()
        
        # creating species
        self.build_species()

        # creating proteins
        self.build_proteins()

        # creating isoforms
        self.build_isoforms()

        # parsing alignment file
        self.parse_alignment_file()

        # creating domains
        self.build_domain_types()
        self.build_domains()

    def parse_file(self):
        with open(os.sep.join([settings.DATA_DIR, 'SH2_domain_containing_prot_struct.csv']), newline='') as csvfile:
            uniprot_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(uniprot_reader):
                if i==0:
                    continue
                if row[6] not in self.families:
                    self.families.append(row[6])
                if row[8] not in self.species:
                    self.species.append(row[8])
                if row[1] not in self.proteins:
                    self.proteins[row[1]] = [row[6],row[7],row[8],row[11]]

    def build_families(self):
        for f in self.families:
            protfam, created = ProteinFamily.objects.get_or_create(parent=None, slug=f.lower(), name=f)
            self.fam_objects[f] = protfam

    def build_species(self):
        for s in self.species:
            sp, created = Species.objects.get_or_create(latin_name=self.species_latin[s], common_name=s.capitalize())
            self.species_objects[s] = sp

    def build_proteins(self):
        for p, vals in self.proteins.items():
            family, gene_name, species, accession = vals
            protein, created = Protein.objects.get_or_create(parent=None, family=self.fam_objects[family], species=self.species_objects[species], entry_name=p.lower(), accession=accession, name=gene_name)

    def build_isoforms(self):
        for p in Protein.objects.all():
            isoform, created = Isoform.objects.get_or_create(protein=p, accession=p.accession+'-1')

    def build_domain_types(self):
        for i in ['N','C']:
            domaintype, created = DomainType.objects.get_or_create(slug=i, name=i+'-terminal')

    def build_domains(self):
        for i, j in self.protein_seqs.items():
            if '_' in i:
                domaintype = DomainType.objects.get(slug=i[-1])
                gene_name = i.split('_')[0]
            else:
                domaintype = DomainType.objects.get(slug='N')
                gene_name = i
            try:
                isoform = Isoform.objects.get(protein__name=gene_name)
            except Isoform.DoesNotExist:
                print('Error: {} Protein not in database'.format(i))
                continue
            seq, created = Sequence.objects.get_or_create(sequence=j)
            domain, created = Domain.objects.get_or_create(domain_type=domaintype, isoform=isoform, sequence=seq, parent=None)

    def parse_alignment_file(self):
        with open(os.sep.join([settings.DATA_DIR, 'table_from_alignment_with_pdbs_0917.csv']), newline='') as csvfile:
            structure_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(structure_reader):
                if row[1]=='seq':
                    self.protein_seqs[row[0]] = ''.join(row[2:]).replace('-','')

