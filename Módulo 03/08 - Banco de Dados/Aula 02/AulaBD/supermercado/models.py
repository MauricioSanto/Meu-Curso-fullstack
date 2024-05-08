from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome
    

class Documento(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    cpf = models.PositiveIntegerField()
    rg = models.FileField(upload_to="rg")

    def __str__(self):
        return self.cliente.nome + " | Documentos"
    


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    estoque = models.IntegerField()
    valor = models.FloatField()
    
    def __str__(self):
        return self.nome
    

class OrdemCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome + " | Ordem de Compra"
    