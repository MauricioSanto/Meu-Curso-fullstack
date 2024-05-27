from django.db import models

class produto (models.Model):
    nome_produto = models.CharField(max_length=50, verbose_name="Nome do Produto")
    valor_produto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= "Valor do Produto")

    def __str__(self):
        return self.nome_produto
    