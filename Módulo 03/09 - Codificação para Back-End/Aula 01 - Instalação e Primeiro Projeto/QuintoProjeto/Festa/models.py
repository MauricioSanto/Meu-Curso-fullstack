from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    Titulo = models.CharField(max_length=100)
    Editora = models.CharField(max_length=80)
    Ano_Publicacao = models.IntegerField()
    artigo = models.CharField(max_length=50 , default="")

    def __str__(self):
        return self.nome
    
class Obra(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=80)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.nome + "|" + str(self.autor)