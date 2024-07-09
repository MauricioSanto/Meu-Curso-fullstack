from django.db import models

class cadastro_funcionarios (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="E-Mail")
    foto = models.ImageField(upload_to="foto_perfil/", null=True, blank=True)
    celular = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.nome
    
class clientes(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    contato = models.IntegerField()
    

    def __str__(self):
        return self.nome
    
class carros (models.Model):
    modelo = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    ano = models.IntegerField()
    foto = models.ImageField(upload_to="foto_perfil/", null=True , blank=True)

    def __str__(self):
        return self.modelo
    
class pagamento(models.Model):
    forma_de_pagamento = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    carro = models.ForeignKey(to=carros, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.OneToOneField(clientes,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.forma_de_pagamento + '|' + str(self.valor)
    
class Pedido(models.Model):
    numero_pedido = models.PositiveIntegerField()
    cliente = models.ForeignKey("clientes",on_delete=models.CASCADE,null=True,blank=True)
    modelo = models.ForeignKey("carros",on_delete=models.CASCADE,null=True,blank=True)
    pagamento = models.ForeignKey("pagamento",on_delete=models.CASCADE,null=True,blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  str(self.numero_pedido)
    