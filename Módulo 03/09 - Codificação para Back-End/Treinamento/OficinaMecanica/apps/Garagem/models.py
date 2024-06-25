from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="E-mail")
    celular = models.PositiveIntegerField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Veiculos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="foto_perfil/")

    def __str__(self):
        return self.placa
    
class OrdemServico(models.Model):
    OrdemNumero = models.PositiveIntegerField()
    data = models.DateTimeField()
    status = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pecas = models.CharField(max_length=100, verbose_name="Peças")
    veiculo = models.ForeignKey(Veiculos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.OrdemNumero)
    
class Pecas (models.Model):
    id_da_peca = models.IntegerField()
    nome_da_peca = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="foto_perfil/")

    def __str__(self):
        return self.nome_da_peca +" | "+ str(self.valor)

class Mecanicos(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="foto_perfil/")


    def __str__(self):
        return self.nome + " | " + self.especialidade

class Vendas (models.Model):
    mecanico = models.ForeignKey(Mecanicos,on_delete=models.CASCADE,verbose_name="Mecânico")
    valor_do_servico = models.ForeignKey(OrdemServico,on_delete=models.CASCADE,verbose_name="Valor do Serviço")
    veiculo = models.ForeignKey(Veiculos,on_delete=models.CASCADE)
    Valor_Total = models.IntegerField()

    def __str__(self):
        return str(self.Valor_Total)
    
    

    

    

                                