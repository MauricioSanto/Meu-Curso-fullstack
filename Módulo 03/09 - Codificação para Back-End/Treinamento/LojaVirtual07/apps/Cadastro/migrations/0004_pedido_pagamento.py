# Generated by Django 5.0.6 on 2024-06-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0003_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='pagamento',
            field=models.ManyToManyField(to='Cadastro.pagamento'),
        ),
    ]
