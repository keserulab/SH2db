from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from protein.models import Protein, ProteinConformation, ProteinState, Species, ProteinFamily, Isoform, Sequence, DomainType, Domain, ProteinSegment
from residue.models import Residue, ResidueNumberingScheme, ResidueGenericNumber
from structure.models import StructureDomain

import csv
import os
import pprint
from Bio.PDB import Polypeptide


class Command(BaseBuild):

    def add_arguments(self, parser):
        parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        parser.add_argument("--purge", default=False, action="store_true", help="Purge data")

    def handle(self, *args, **options):
        sd = StructureDomain.objects.all()
        for s in sd:
            print(s.domain.isoform.protein.name, s.chain.chain_ID, s.domain.domain_type.slug, s.chain.structure.pdb_code, len(s.domain.sequence.sequence), len(Residue.objects.filter(domain=s.domain)))