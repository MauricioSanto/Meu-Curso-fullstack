# Generated by Django 5.0.4 on 2024-05-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parte2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosaluno',
            name='foto_perfil',
            field=models.ImageField(upload_to='perfil/'),
        ),
    ]
