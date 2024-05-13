from django.db import models

class carros(models.Model):
    Marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    Ano_fabricacao = models.IntegerField()
    Km = models.IntegerField()
    Preço = models.FloatField()

    def __str__(self):
        return self.modelo + "|" + str(self.Preço)
    
class vendedor(models.Model):
    Nome = models.CharField(max_length=100)
    Matricula = models.IntegerField()
    Carro = models.ForeignKey(carros,on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.Nome + "|" + str(self.Matricula)