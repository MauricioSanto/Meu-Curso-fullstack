from django.shortcuts import render
from .models import *

def VerProdutos(request):
    produtos_lista = produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos_lista})


def LinkInicial(request):
    return render(request, "index.html")

def LinkCadastro(request):
    return render(request, "cadastro.html")


