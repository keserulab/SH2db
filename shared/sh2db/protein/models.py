from django.db import models

class Protein(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    family = models.ForeignKey('ProteinFamily', on_delete=models.CASCADE)
    species = models.ForeignKey('Species', on_delete=models.CASCADE)
    entry_name = models.SlugField(max_length=100, unique=True)
    accession = models.CharField(max_length=100, db_index=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
    	return self.entry_name

    class Meta():
        db_table = 'protein'


class ProteinConformation(models.Model):
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    state = models.ForeignKey('ProteinState', on_delete=models.CASCADE)

    def __str__(self):
        return '<{}-{}>'.format(self.domain.isoform.protein.entry_name, self.state.slug)

    class Meta():
        ordering = ('id', )
        db_table = "protein_conformation"


class ProteinState(models.Model):
    slug = models.SlugField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.slug

    class Meta():
        db_table = "protein_state"


class ProteinSegment(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    fully_aligned = models.BooleanField(default=False)
    partial = models.BooleanField(default=False)
    proteinfamily = models.CharField(max_length=20)

    def __str__(self):
        return self.slug

    class Meta():
        ordering = ('id', )
        db_table = 'protein_segment'
        unique_together = ('slug', 'proteinfamily')


class Species(models.Model):
    latin_name = models.CharField(max_length=100, unique=True)
    common_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.latin_name

    class Meta():
        db_table = 'species'


class ProteinFamily(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'protein_family'


class Isoform(models.Model):
	protein = models.ForeignKey('Protein', on_delete=models.CASCADE)
	accession = models.CharField(max_length=100, db_index=True, null=True)

	def __str__(self):
		return '<{}-{}>'.format(self.protein.entry_name, self.accession)

	class Meta():
		db_table = 'protein_isoform'


class Domain(models.Model):
    domain_type = models.ForeignKey('DomainType', on_delete=models.CASCADE)
    isoform = models.ForeignKey('Isoform', on_delete=models.CASCADE)
    sequence = models.ForeignKey('Sequence', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '<{}-{}>'.format(self.isoform.protein.entry_name, self.domain_type.name)

    class Meta():
        db_table = 'protein_domain'


class DomainType(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'protein_domaintype'


class Sequence(models.Model):
    sequence = models.TextField()

    def __str__(self):
        return self.sequence

    class Meta():
        db_table = 'sequence'
