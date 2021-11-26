from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from protein.models import Domain
from common.models import Publication

# Create your models here.

class Structure(models.Model):
    pdb_code = models.CharField(max_length=4, unique=True)
    publication_date = models.DateField()
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    resolution = models.DecimalField(max_digits=5, decimal_places=3)
    structure_type = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.pdb_code

    class Meta():
        db_table = 'structure'


class Chain(models.Model):
    chain_ID = models.CharField(max_length=1)
    structure = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.chain_ID

    class Meta():
        db_table = 'chain'


class StructureDomain(models.Model):
    chain = models.ForeignKey('self', on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    sequence = models.ForeignKey('self', on_delete=models.CASCADE)
    pdbdata = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.domain, self.chain)

    class Meta():
        db_table = 'structure_domain'


class StructureType(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'structure_type'


class PDBData():
    pdb = models.TextField()

    def __str__(self):
        return ('pdb data object')

    class Meta():
        db_table = 'pdbdata'