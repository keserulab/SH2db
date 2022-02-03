from django.db import models
from django.db.models.base import Model

# Create your models here.

class Publication(models.Model):
    journal = models.TextField(null=True)
    title = models.TextField(null=True)
    authors = models.TextField(null=True)
    year = models.IntegerField(null=True)
    reference = models.TextField(null=True)

    def __str__(self):
    	return '{}-{}-{}...'.format(self.journal, self.year, self.title[:10])

    class Meta():
        db_table = 'publication'
