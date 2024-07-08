# Generated by Django 5.0.6 on 2024-07-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto_media/')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
