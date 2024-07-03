from django.shortcuts import render, redirect
from .models import *
from .forms import *

def VerFuncionario(request):
    produtos_lista = cadastro_funcionarios.objects.all()
    return render(request, 'Funcionarios.html', {'colaborador': produtos_lista})

def LinkInicial(request):
    return render(request, "index.html")

def LinkCadastroFuncionario(request):
    produtos_lista = cadastro_funcionarios.objects.all()
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


def DetalhesCarro(request, id_carro):
    busca = carros.objects.get(id=id_carro)
    return render(request, "detalhes_carros.html", {"carros": busca})

def PedidosCarros (request):
    pedidos_lista = Pedido.objects.all()
    return render(request, "pedido.html", {"pedidos":pedidos_lista} )

def CriarCarros(request):
    busca_carro = carros.objects.all()
    if request.method == "POST":
        novo_carro = FormularioCarros(request.POST, request.FILES)
        if novo_carro.is_valid():
            novo_carro.save()
            return redirect("pagina_cadastro")
    else:
        novo_carro = FormularioCarros()
    return render(request, "cadastro.html", {"formulario": novo_carro, "carro": busca_carro})

