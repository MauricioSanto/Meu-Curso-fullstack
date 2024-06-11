from django.db import models

class carro(models.Model):
    nome = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    ano = models.DateField()
    foto = models.ImageField(upload_to="foto_perfil/", default=True)

    def __str__(self):
        return self.nome
    