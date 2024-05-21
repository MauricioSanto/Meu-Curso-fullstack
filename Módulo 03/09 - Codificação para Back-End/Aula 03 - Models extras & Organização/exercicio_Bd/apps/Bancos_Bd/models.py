from django.db import models

class Clientes (models.Model):
    Nome = models.CharField(max_length=50)
    Endereco = models.CharField(max_length=100, verbose_name='Endereço')
    cpf = models.IntegerField(verbose_name='CPF')
    E_Mail = models.EmailField(verbose_name='E-Mail')

    def __str__(self):
        return self.Nome
    
class Produtos (models.Model):
    Nome_produto = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=200, verbose_name='Descrição')
    preco = models.DecimalField(decimal_places=2,max_digits=8, verbose_name='Preço')
    secao = models.CharField(max_length=10, verbose_name='Seção')

    def __str__(self):
        return self.Nome_produto
    
class Transportadora (models.Model):
    nome_da_Transportadora = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    fone = models.IntegerField(verbose_name='Celular')
    E_Mail = models.EmailField(verbose_name='E-Mail')

    def __str__(self):
        return self.nome_da_Transportadora
    
class Funcionario (models.Model):
    nome = models.CharField(max_length=100)
    Matricula = models.IntegerField()
    Cargo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="foto_perfil/")

    
    def __str__(self):
        return self.nome
    
class Pedidos (models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    Data_do_pedido = models.DateField(auto_now=True)
    produto = models.ManyToManyField(Produtos)
    valor = models.FloatField()
    transporte = models.ForeignKey(Transportadora, on_delete=models.CASCADE)
    Numero_do_Pedido = models.IntegerField()
    Vendedor = models.ManyToManyField(Funcionario)

    def __str__(self):
        return str(self.Numero_do_Pedido)
        
    

    
    


    
    




    

