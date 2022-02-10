from django.core.management.base import BaseCommand, CommandError
from build.management.commands.base_build import Command as BaseBuild
from django.conf import settings
from django.db import connection
from django.db import IntegrityError

from common.models import WebResource

import os, csv


class Command(BaseBuild):

    web_resources = os.sep.join([settings.DATA_DIR, 'resources.csv'])

    def add_arguments(self, parser):
        parser.add_argument("--debug", default=False, action="store_true", help="Debug mode")
        parser.add_argument("--purge", default=False, action="store_true", help="Purge data")

    def handle(self, *args, **options):
        if options['purge']:
            WebResource.objects.all().delete()

        self.build_web_resource()

    def build_web_resource(self):
        with open(self.web_resources, newline='') as csvfile:
            wr_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(wr_reader):
                wr, created = WebResource.objects.get_or_create(slug=row[0], name=row[1], url=row[2])