from django.db import models


class Residue(models.Model):
    domain = models.ForeignKey('protein.Domain', on_delete=models.CASCADE)
    protein_segment = models.ForeignKey('protein.ProteinSegment', null=True, on_delete=models.CASCADE)
    generic_number = models.ForeignKey('ResidueGenericNumber', related_name='compare', null=True, on_delete=models.CASCADE)
    sequence_number = models.SmallIntegerField()
    amino_acid = models.CharField(max_length=1)
    amino_acid_three_letter = models.CharField(max_length=3)

    def __str__(self):
        return self.amino_acid + str(self.sequence_number)

    class Meta():
        db_table = 'residue'
        ordering = ['sequence_number']


class ResidueGenericNumber(models.Model):
    scheme = models.ForeignKey('ResidueNumberingScheme', on_delete=models.CASCADE)
    protein_segment = models.ForeignKey('protein.ProteinSegment', related_name='generic_numbers', null=True, on_delete=models.CASCADE)
    label = models.CharField(db_index=True, max_length=12)

    def __str__(self):
        return self.label

    class Meta():
        db_table = 'residue_generic_number'
        unique_together = ('scheme', 'label')


class ResidueNumberingScheme(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20)
    short_name = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'residue_generic_numbering_scheme'
