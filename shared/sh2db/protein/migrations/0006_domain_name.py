# Generated by Django 3.2.8 on 2022-02-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0005_proteinsegment'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='name',
            field=models.SlugField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
