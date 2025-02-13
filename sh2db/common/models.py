from django.db import models


class Publication(models.Model):
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE, null=True)
    title = models.TextField(null=True)
    authors = models.TextField(null=True)
    year = models.IntegerField(null=True)
    reference = models.ForeignKey('WebLink', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}-{}-{}...'.format(self.journal, self.year, self.title[:10])

    class Meta():
        db_table = 'publication'


class Journal(models.Model):
	name = models.TextField()

	def __str__(self):
		return '<{}>'.format(self.name)

	class Meta():
		db_table = 'journal'


class WebLink(models.Model):
	web_resource = models.ForeignKey('WebResource', on_delete=models.CASCADE)
	index = models.TextField()

	def __str__(self):
		return '<{}: {}>'.format(self.web_resource.name, self.index)

	class Meta():
		db_table = 'web_link'


class WebResource(models.Model):
	slug = models.SlugField()
	name = models.TextField()
	url = models.TextField()

	def __str__(self):
		return '<{}>'.format(self.name)

	class Meta():
		db_table = 'web_resource'
