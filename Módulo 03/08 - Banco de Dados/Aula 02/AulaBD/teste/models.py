from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobre_voce = models.TextField()
    idade = models.IntegerField()
    altura = models.FloatField()
    possui_filhos = models.BooleanField(default=False, verbose_name="Possui filho(s)?")
    data_nascimento = models.DateField(null=True)
    data_de_criacao = models.DateTimeField(null=True, verbose_name="Data de criação")

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Editora(models.Model):
    nome_editora = models.CharField(max_length=100)
    livros_produzidos = models.ManyToManyField(Livro)

    def __str__(self):
        return self.nome_editora
