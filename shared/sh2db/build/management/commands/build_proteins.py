from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from protein.models import Protein, ProteinConformation, ProteinState, Species, ProteinFamily, Isoform, Sequence, DomainType, Domain, ProteinSegment
from residue.models import Residue, ResidueNumberingScheme, ResidueGenericNumber

import csv
import os
import pprint
from Bio.PDB import Polypeptide


class Command(BaseBuild):

    species_latin = {'HUMAN':'Homo sapiens'}
    families = []
    proteins = {}
    species = []
    fam_objects = {}
    species_objects = {}
    protein_seqs = {}
    protein_seqs_aligned = {}
    gns = []
    seqnums = {}

    def add_arguments(self, parser):
        parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        parser.add_argument("--purge", default=False, action="store_true", help="Purge data")

    def handle(self, *args, **options):
        if options['purge']:
            Protein.objects.all().delete()
            ProteinFamily.objects.all().delete()
            Species.objects.all().delete()
            Residue.objects.all().delete()

        # parsing data file
        self.parse_file()
 
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

        # residues
        self.build_protein_residues()

    def parse_file(self):
        with open(os.sep.join([settings.DATA_DIR, 'protein_data.csv']), newline='') as csvfile:
            uniprot_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(uniprot_reader):
                if row[0] not in self.families:
                    self.families.append(row[0])
                if row[2] not in self.species:
                    self.species.append(row[2])
                entry_name = row[1]+'_'+row[2]
                if entry_name not in self.proteins:
                    self.proteins[entry_name] = [row[0],row[1],row[2],row[3]]

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

    def build_protein_residues(self):
        for i, seqnums in self.seqnums.items():
            if '_' in i:
                name, domaintype = i.split('_')
            else:
                name = i
                domaintype = 'N'
            domain = Domain.objects.get(parent__isnull=True, isoform__protein__name=name, domain_type__slug=domaintype)
            resis = []
            for j, seqnum in enumerate(seqnums):
                if seqnum in ['',' ','-']:
                    continue
                if self.gns[j]!='':
                    seg = ProteinSegment.objects.get(name=self.gns[j][:-2])
                else:
                    seg = self.find_segment(j)
                gn = self.gns[j]
                if gn=='':
                    gn = None
                else:
                    gn = ResidueGenericNumber.objects.get(label=gn)
                aa = self.protein_seqs_aligned[i][j]
                res = Residue()
                res.domain = domain
                res.protein_segment = seg
                res.generic_number = gn
                res.sequence_number = int(seqnum)
                res.amino_acid = aa
                res.amino_acid_three_letter = Polypeptide.one_to_three(aa)
                resis.append(res)
            Residue.objects.bulk_create(resis)

    def find_segment(self, position):
        next_seg, prev_seg = False, False
        for gn in self.gns[position:]:
            if gn!='':
                next_seg = gn[:2]
                break
        if not next_seg:
            seg = ProteinSegment.objects.get(name='C-term')
        for i in range(len(self.gns[:position]),0,-1):
        # for gn in self.gns[:position+1].reverse():
            gn = self.gns[i]
            if gn not in ['',' ','-']:
                prev_seg = gn[:-2]
                break
        if not prev_seg:
            seg = ProteinSegment.objects.get(name='N-term')
        if next_seg and prev_seg:
            seg = ProteinSegment.objects.get(name=prev_seg+next_seg)
        return seg

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
        scheme = ResidueNumberingScheme.objects.get(short_name='GN')
        with open(os.sep.join([settings.DATA_DIR, 'table_from_alignment_with_pdbs_0917.csv']), newline='') as csvfile:
            structure_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(structure_reader):
                if i==1:
                    self.gns = row[2:]
                    for j, gn in enumerate(row):
                        if gn not in ['',' ']:
                            segment = ProteinSegment.objects.get(name=gn[:-2])
                            gn = ResidueGenericNumber.objects.get_or_create(label=gn, protein_segment=segment, scheme=scheme)

                if row[1]=='seq':
                    self.protein_seqs[row[0]] = ''.join(row[2:]).replace('-','')
                    self.protein_seqs_aligned[row[0]] = row[2:]
                if row[1]=='nums':
                    self.seqnums[row[0]] = row[2:]
