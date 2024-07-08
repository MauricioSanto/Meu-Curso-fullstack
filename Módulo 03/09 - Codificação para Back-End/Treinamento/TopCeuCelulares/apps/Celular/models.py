from django.db import models

class celular(models.Model):
    foto = models.ImageField(upload_to="foto_media/", null=True, blank=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name="Descrição")
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
    

