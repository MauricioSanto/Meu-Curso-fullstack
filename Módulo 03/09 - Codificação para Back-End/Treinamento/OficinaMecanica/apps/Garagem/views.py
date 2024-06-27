from django.shortcuts import render, redirect
from .models import *
from .forms import *

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

def CriarClientes(request):
    busca_Clientes = Clientes.objects.all()
    if request.method == "POST":
        novo_cliente = FormularioClientes(request.POST)
        novo_cliente.save()
        novo_cliente = FormularioClientes()
    else:
        novo_cliente = FormularioClientes()
    return render(request, "clientes.html", {"formulario": novo_cliente, "clientes": busca_Clientes})

def CriarMecanico(request):
    busca_mecanico = Mecanicos.objects.all()
    if request.method == "POST":
        novo_mecanico = FormularioMecanico(request.POST, request.FILES)
        novo_mecanico.save()
        novo_mecanico = FormularioMecanico()
    else:
        novo_mecanico = FormularioMecanico()
    return render(request, "mecanico.html", {"formulario": novo_mecanico, "mecanico": busca_mecanico})

def CriarOrdemServico(request):
    busca_Os = OrdemServico.objects.all()
    if request.method == "POST":
        novo_Os = FormularioOrdemServico(request.POST)
        novo_Os.save()
        novo_Os = FormularioOrdemServico()
    else:
        novo_Os = FormularioOrdemServico()
    return render(request, "OrdemServico.html", {"formulario": novo_Os, "Ordem": busca_Os})


def CriarVeiculo(request):
    busca_veiculo = Veiculos.objects.all()
    if request.method == "POST":
        novo_veiculo = FormularioVeiculos(request.POST, request.FILES)
        novo_veiculo.save()
        novo_veiculo = FormularioVeiculos()
    else:
        novo_veiculo = FormularioVeiculos()
    return render(request, "veiculos.html", {"formulario": novo_veiculo, "veiculo": busca_veiculo})


def CriarPecas(request):
    busca_pecas = Pecas.objects.all()
    if request.method == "POST":
        novo_pecas = FormularioPecas(request.POST, request.FILES)
        novo_pecas.save()
        novo_pecas = FormularioPecas()
    else:
        novo_pecas = FormularioPecas()
    return render(request, "pecas.html", {"formulario": novo_pecas, "pecas": busca_pecas})


def CriarVendas(request):
    busca_vendas = Vendas.objects.all()
    if request.method == "POST":
        novo_vendas = FormularioVendas(request.POST)
        novo_vendas.save()
        novo_vendas = FormularioVendas()
    else:
        novo_vendas = FormularioVendas()
    return render(request, "vendas.html", {"formulario": novo_vendas, "vendas": busca_vendas})







# Create your views here.
