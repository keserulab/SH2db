# Generated by Django 3.2.8 on 2022-03-24 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_auto_20220324_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chain',
            options={'ordering': ['chain_ID']},
        ),
    ]
