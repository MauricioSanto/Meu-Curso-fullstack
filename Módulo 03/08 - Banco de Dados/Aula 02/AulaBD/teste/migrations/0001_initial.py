# Generated by Django 5.0.4 on 2024-04-23 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobreVoce', models.TextField()),
                ('idade', models.IntegerField()),
                ('altura', models.FloatField()),
                ('PCD', models.BooleanField(default=False)),
                ('data', models.DateField()),
                ('data_e_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.pessoa')),
            ],
        ),
    ]
