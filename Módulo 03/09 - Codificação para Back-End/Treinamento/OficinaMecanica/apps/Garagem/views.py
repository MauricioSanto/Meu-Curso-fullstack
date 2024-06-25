from django.shortcuts import render
from .models import *

def Inicio(request):
    return render(request,'index.html')

def VerClientes(request):
    Clientes_lista = Clientes.objects.all()
    return render(request, 'clientes.html', {'cliente': Clientes_lista})

def VerVeiculos(request):
    veiculos_lista = Veiculos.objects.all()
    return render(request, 'veiculos.html', {'veiculo': veiculos_lista})

def VerOrdemServico(request):
    OrdemServico_lista = OrdemServico.objects.all()
    return render(request, 'OrdemServico.html', {'servico': OrdemServico_lista})

def VerPecas(request):
    Pecas_lista = Pecas.objects.all()
    return render(request, 'pecas.html', {'pecas': Pecas_lista})

def VerMecanicos(request):
    Mecanicos_lista = Mecanicos.objects.all()
    return render(request, 'mecanico.html', {'mecanico': Mecanicos_lista})

def VerVendas(request):
    Vendas_lista = Vendas.objects.all()
    return render(request, 'vendas.html', {'venda': Vendas_lista})



# Create your views here.
