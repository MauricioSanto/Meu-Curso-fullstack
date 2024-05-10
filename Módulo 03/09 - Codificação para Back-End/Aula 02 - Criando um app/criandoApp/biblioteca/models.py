from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
