# Generated by Django 5.0.6 on 2024-05-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Madeiras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='produto',
            field=models.CharField(max_length=50),
        ),
    ]
