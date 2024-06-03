from django.db import models

class cliente (models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.IntegerField(verbose_name='CPF')

    def __str__(self):
        return self.nome
    
