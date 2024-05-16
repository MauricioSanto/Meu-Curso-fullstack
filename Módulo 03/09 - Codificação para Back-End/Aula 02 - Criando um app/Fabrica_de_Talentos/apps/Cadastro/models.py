from django.db import models

class Cadastros (models.Model):
    Tipo_sexo = (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )

    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    cpf = models.PositiveIntegerField(verbose_name="CPF")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    E_mail = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.nome
    
    sexo = models.CharField(max_length=2, choices=Tipo_sexo)

class Talento(models.Model):
    Habilidade = models.CharField(max_length=100)
    Nota = models.IntegerField()
    nomes = models.ForeignKey(Cadastros,on_delete=models.CASCADE)

    def __str__(self):
        return self.Habilidade 
    
    
