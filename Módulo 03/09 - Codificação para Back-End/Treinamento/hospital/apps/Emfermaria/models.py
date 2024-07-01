from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
# Create your models here.
