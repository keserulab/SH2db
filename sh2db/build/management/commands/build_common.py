from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from common.models import WebResource
from residue.models import ResidueNumberingScheme
from protein.models import ProteinSegment

import os, csv


class Command(BaseBuild):

    web_resources = os.sep.join([settings.DATA_DIR, 'resources.csv'])
    protein_segments = os.sep.join([settings.DATA_DIR, 'protein_segments.csv'])

    def add_arguments(self, parser):
        parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        parser.add_argument("--purge", default=False, action="store_true", help="Purge data")

    def handle(self, *args, **options):
        if options['purge']:
            WebResource.objects.all().delete()

        self.build_web_resource()
        self.build_numbering_schemes()
        self.build_protein_segments()

    def build_web_resource(self):
        with open(self.web_resources, newline='') as csvfile:
            wr_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(wr_reader):
                wr, created = WebResource.objects.get_or_create(slug=row[0], name=row[1], url=row[2])

    def build_numbering_schemes(self):
        ns, created = ResidueNumberingScheme.objects.get_or_create(parent=None, slug='gn', short_name='GN', name='SH2db generic number')

    def build_protein_segments(self):
        with open(self.protein_segments, newline='') as csvfile:
            ps_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in ps_reader:
                if row[1] in ['sheet','helix']:
                    aligned = True
                else:
                    aligned = False

                seg, created = ProteinSegment.objects.get_or_create(slug=row[0], name=row[0], category=row[1], proteinfamily='SH2', fully_aligned=aligned)
