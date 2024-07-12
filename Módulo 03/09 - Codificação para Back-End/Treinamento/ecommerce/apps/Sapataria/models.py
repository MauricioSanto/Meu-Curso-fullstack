from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField( verbose_name= "CPF:")
    end = models.CharField(max_length=100, verbose_name="Endereço:")

    def __str__(self):
        return self.nome
      
class Sapato(models.Model):
    foto = models.ImageField(upload_to="foto_media/", blank=True)
    marca = models.CharField(max_length=100)
    tamanho = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.marca
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Sapato)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"
