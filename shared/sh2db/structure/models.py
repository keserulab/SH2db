from django.db import models


class Structure(models.Model):
    pdb_code = models.CharField(max_length=4, unique=True)
    publication_date = models.DateField()
    publication = models.ForeignKey('common.Publication', on_delete=models.CASCADE)
    resolution = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    structure_type = models.ForeignKey('StructureType', on_delete=models.CASCADE)

    def __str__(self):
        return self.pdb_code

    class Meta():
        db_table = 'structure'


class Chain(models.Model):
    chain_ID = models.CharField(max_length=1)
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE, related_name='chain')

    def __str__(self):
        return self.chain_ID

    class Meta():
        db_table = 'chain'
        ordering = ['chain_ID']


class StructureDomain(models.Model):
    chain = models.ForeignKey('Chain', on_delete=models.CASCADE, related_name='structure_domain')
    domain = models.ForeignKey('protein.Domain', on_delete=models.CASCADE, related_name='structure_domain')
    pdbdata = models.ForeignKey('PDBData', on_delete=models.CASCADE)
    #name = models.SlugField(max_length=100, unique=True)
    #sequence = models.ForeignKey('protein.Sequence', on_delete=models.CASCADE)

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


class PDBData(models.Model):
    pdb = models.TextField()

    def __str__(self):
        return ('pdb data object')

    class Meta():
        db_table = 'pdbdata'
