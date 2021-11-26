from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from protein.models import Domain

# Create your models here.

# NULL-okat ki venni onnan, ahol nem kellenek
# Unique-okat is átnézni

# Amikor kész a structure model -> le kell futtatni: make migrations (megnézi, hogy bármelyik models.py-ban történt-e változás
#   -> ahol történt változás ott létrejönnek migration file-ok --> push github-ra -> pull -> migrate parancs --> megváltoztatja az adatbázis szerkezetét)

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
    structure = models.ForeignKey('self', null = True, on_delete=models.CASCADE) # Itt kérdés, hogy maradhat-e  NULL, mert nem minden szerkezet egyforma hosszú. Ha ez egy tábla az összes szerkezetre, akkor maradnia kell NULL-nak, ha adott szerkezetre vonatkozik mennie kell

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
        return self.chain

    class Meta():
        db_table = 'structure_domain'


class StructureType(models.Model):
    slug = models.SlugField() # X-ray
    name = models.CharField(max_length=20) # X-ray Crystallography

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