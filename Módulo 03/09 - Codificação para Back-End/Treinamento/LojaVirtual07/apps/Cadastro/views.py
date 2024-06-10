from django.shortcuts import render
from .models import *

def VerFuncionario(request):
    produtos_lista = cadastro.objects.all()
    return render(request, 'index.html', {'colaborador': produtos_lista})

def LinkInicial(request):
    return render(request, "index.html")

def LinkCadastro(request):
    return render(request, "cadastro.html")


