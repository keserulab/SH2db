from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from common.alignment import Alignment
from protein.models import Domain

import os, csv

from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo
from Bio import AlignIO
import pylab
import matplotlib.pyplot as plt
import networkx as nx
from ete3 import Tree


class Command(BaseBuild):

    def add_arguments(self, parser):
        # parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        # parser.add_argument("--purge", default=False, action="store_true", help="Purge data")
        pass

    def handle(self, *args, **options):
        self.create_fasta_file()
        aln = AlignIO.read('./proteins_annotated_segments.fasta', 'fasta')
        calculator = DistanceCalculator('blosum62')
        dm = calculator.get_distance(aln)
        constructor = DistanceTreeConstructor(calculator, 'nj')
        tree = constructor.build_tree(aln)
        Phylo.write(tree, './tree.xml', 'phyloxml')
        # Phylo.convert('./tree.xml', 'phyloxml', './tree.nhx', 'newick')
        # nw = Phylo.NewickIO.write([tree], './tree.nhx')
        # with open('./tree.nhx', 'r') as f1:
        #     tree = f1.read()
        # print(tree)
        Phylo.draw(tree)
        pylab.savefig('tree.svg',format='svg', dpi=300)

        # t = Tree(tree)
        # t.show()

    def create_fasta_file(self):
        domains = Domain.objects.filter(parent__isnull=True).order_by('isoform', 'domain_type', '-parent', 'name')

        alignment = Alignment(domains)
        segments, gns, residues = alignment.align_domain_residues()

        gn_indeces = []
        for i, gn in enumerate(gns):
            if gn!='':
                gn_indeces.append(i+2)

        out = ''
        for line in residues:
            if line[1].name=='N-terminal':
                this_header = '>{}'.format(line[0])
            else:
                this_header = '>{}-C'.format(line[0])
            this_seq = ''
            full_seq = ''
            for j in line:
                if j=='-':
                    full_seq+=j
                try:
                    full_seq+=j.amino_acid
                except:
                    pass
            for i in gn_indeces:
                if line[i]!='-':
                    this_seq+=line[i].amino_acid
                else:
                    this_seq+=line[i]
            print(this_header)
            print(this_seq)
            out+=this_header+'\n'
            out+=this_seq+'\n'
        with open('./proteins_annotated_segments.fasta', 'w') as f1:
            f1.write(out)
