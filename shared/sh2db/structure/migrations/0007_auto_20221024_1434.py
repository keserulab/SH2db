# Generated by Django 3.2.8 on 2022-10-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20220208_1242'),
        ('structure', '0006_auto_20220505_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structure',
            name='pdb_code',
            field=models.CharField(max_length=4, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='structure',
            name='publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.publication'),
        ),
    ]
