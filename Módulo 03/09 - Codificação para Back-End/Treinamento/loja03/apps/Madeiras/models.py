from django.db import models

class clientes (models.Model):
    nome = models.CharField(max_length=100,verbose_name='Nome:')
    celular = models.IntegerField(verbose_name='Celular')
    end = models.CharField(max_length=100, verbose_name='Endereço')
    cpf = models.PositiveIntegerField(verbose_name='CPF')

    def __str__(self):
        return self.nome
    
class fornecedor (models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome') 
    contato = models.CharField(max_length=50, verbose_name='Contato') 
    celular = models.IntegerField(verbose_name='Celular')  
    email = models.EmailField(verbose_name='E-mail')
    produto = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    
class estoque (models.Model):
    produto = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    dataEntrada = models.DateField()

    def __str__(self):
        return self.produto
    
    
class produtos (models.Model):
    nome = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(fornecedor, on_delete=models.CASCADE)
    estoque = models.ForeignKey(estoque, on_delete=models.CASCADE)
    dataEntrada = models.DateField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    foto = models.ImageField(upload_to="foto_perfil/", default=True)

    def __str__(self):
        return self.nome
    
    
class vendas (models.Model):
    venda = models.IntegerField()
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    produto = models.ForeignKey(produtos,on_delete=models.CASCADE)
    dataCompra = models.DateField()
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.venda)
    
    
    
    
