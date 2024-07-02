from django.db import models

class DVD (models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="foto_perfil/",null=True ,blank=True)
    fabricacao = models.DateField()
    produtora = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo + " | " + self.produtora
    

