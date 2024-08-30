from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to="foto_perfil")
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.PositiveIntegerField()

    def __str__(self):
        return self.razao_social

class Categoria(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Servico(models.Model):
    tipo_servico = models.CharField(max_length=100)
    valor_servico = models.DecimalField(decimal_places=2, max_digits=10)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tipo_servico

class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa =  models.ForeignKey(Empresa, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateTimeField(blank=True, null=True)
    data_finalizacao = models.DateTimeField(blank=True, null=False)
    status = models.BooleanField(blank=True, null=True)
    def __str__(self):
        return "OS: " + self.id + " | " + self.cliente.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(verbose_name="Descrição" ,null=False, blank=True)

    def __str__(self):
        return self.nome
    
class Imagem(models.Model):
    descricao = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='imagens/')
    
    def __str__(self):
        return self.descricao
    