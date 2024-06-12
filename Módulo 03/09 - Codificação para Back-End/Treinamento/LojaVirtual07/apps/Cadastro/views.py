from django.shortcuts import render
from .models import *

def VerFuncionario(request):
    produtos_lista = cadastro.objects.all()
    return render(request, 'Funcionarios.html', {'colaborador': produtos_lista})

def LinkInicial(request):
    return render(request, "index.html")

def LinkCadastro(request):
    produtos_lista = cadastro.objects.all()
    return render(request, "Funcionarios.html", {'colaborador': produtos_lista})

def LinkClientes(request):
    clientes_lista = clientes.objects.all()
    return render(request, "Clientes.html", {'cliente': clientes_lista})

def Linkcarros(request):
    carros_lista = carros.objects.all()
    return render(request, "carros.html", {'carro': carros_lista})

def Linkpagamento(request):
    pagamento_lista = pagamento.objects.all()
    return render(request, "Pagamentos.html", {'pagamentos': pagamento_lista})


