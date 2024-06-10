from django.db import models

class cadastro (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="E-Mail")
    foto = models.ImageField(upload_to="foto_perfil/", default=True)
    celular = models.IntegerField(default=True)

    def __str__(self):
        return self.nome
    