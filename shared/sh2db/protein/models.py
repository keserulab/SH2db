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
	sequence = models.TextField()

	def __str__(self):
		return '{}-{}'.format(self.protein.entry_name, accession)

	class Meta():
		db_table = 'protein_isoform'