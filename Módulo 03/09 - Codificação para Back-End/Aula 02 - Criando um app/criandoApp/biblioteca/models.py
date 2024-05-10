from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
class livro(models.Model):
    isbn = models.IntegerField()  
    livro_nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE, default="")
    editora = models.CharField(max_length=50, default="")
    editora2 = models.CharField(max_length=50, null=True, blank=True)
    editora3 = models.CharField(max_length=50)

    def __str__(self):
        return self.livro_nome  + "|" + str(self.isbn)
    