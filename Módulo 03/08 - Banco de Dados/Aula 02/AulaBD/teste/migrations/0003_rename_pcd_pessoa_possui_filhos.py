# Generated by Django 5.0.4 on 2024-04-23 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_rename_sobrevoce_pessoa_sobre_voce_editora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='PCD',
            new_name='possui_filhos',
        ),
    ]
