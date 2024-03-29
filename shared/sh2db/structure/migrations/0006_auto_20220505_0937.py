# Generated by Django 3.2.8 on 2022-05-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0006_domain_name'),
        ('structure', '0005_alter_chain_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='protein',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='structure', to='protein.protein'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='structuredomain',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='structure_domain', to='protein.domain'),
        ),
    ]
