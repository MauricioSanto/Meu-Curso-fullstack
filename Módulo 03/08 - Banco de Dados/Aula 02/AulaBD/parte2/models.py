from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class DadosAluno(models.Model):
    idade = models.PositiveIntegerField()
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to="perfil/")
    documentos = models.FileField(upload_to="documentos/")
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.aluno.nome + " | Documentos"

@receiver(pre_delete, sender=DadosAluno)
def deletar_arquivo(sender, instance, **kwargs):
    # Exclui o arquivo associado ao campo foto_perfil
    if instance.foto_perfil:
        if os.path.isfile(instance.foto_perfil.path):
            os.remove(instance.foto_perfil.path)
    
    if instance.documentos:
        if os.path.isfile(instance.documentos.path):
            os.remove(instance.documentos.path)
