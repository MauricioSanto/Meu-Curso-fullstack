from django.db import models


class clientes(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    E_mail = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.nome
    
