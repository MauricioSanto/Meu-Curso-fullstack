from django.db import models

class Aula (models.Model):
    status = (
        ("y", "Assistida"),
        ("n", "Não assistida")
    )
    titulo = models.CharField(max_length=100 , verbose_name="Título")
    professor = models.CharField(max_length=100)
    aula_status = models.CharField(max_length=2, choices=status)
    valor_aula = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.titulo
    
    class meta:
        ordering = ('pk',)
        verbose_name = "@Aula"
        verbose_name_plural = "@Aulas"
    
    

