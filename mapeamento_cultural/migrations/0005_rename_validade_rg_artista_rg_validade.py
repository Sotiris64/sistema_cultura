# Generated by Django 3.2.15 on 2022-09-20 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapeamento_cultural', '0004_artista_validade_rg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artista',
            old_name='validade_rg',
            new_name='rg_validade',
        ),
    ]
