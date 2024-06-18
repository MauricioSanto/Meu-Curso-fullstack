from django.shortcuts import render
from .models import *

def VerClientes (request):
    clientes_lista = clientes.objects.all()
    return render(request,'index.html', {'cliente':clientes_lista})

def VerIndex (request):
    return render(request, 'index.html')

def VerLogin (request):
    return render (request, 'login.html')

def LinkInicial(request):
    return render(request, "index.html")

def LinkLogin(request):
    return render(request, "login.html")

def DetalhesCliente(request, id_cliente):
    busca = clientes.objects.get(id=id_cliente)
    return render(request, "detalhes_Clientes.html", {"Cliente": busca})
