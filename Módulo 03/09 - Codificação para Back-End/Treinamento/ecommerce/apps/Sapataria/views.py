from django.shortcuts import render,redirect
from .models import *
from .forms import *

def paginaindex(request):
    return render(request,'index.html')

def CadastroSapato(request):
    busca_sapato = Sapato.objects.all()
    if request.method == "POST":
        novo_sapato = formularioSapato(request.POST, request.FILES)
        if novo_sapato.is_valid():
            novo_sapato.save()
            return redirect("pagina_inicial")
    else:
        novo_sapato = formularioSapato()
    return render(request, "cadastroSapato.html", {"formulario": novo_sapato, "sapatos": busca_sapato})

def CadastroCliente(request):
    busca_cliente = Cliente.objects.all()
    if request.method == "POST":
        novo_cliente = formularioCliente(request.POST)
        if novo_cliente.is_valid():
            novo_cliente.save()
            return redirect("pagina_inicial")
    else:
        novo_cliente = formularioCliente()
    return render(request, "cadastroCliente.html", {"formulario": novo_cliente, "clientes": busca_cliente})

def CadastroPedido(request):
    busca_pedido = Pedido.objects.all()
    if request.method == "POST":
        novo_pedido = formularioPedido(request.POST)
        if novo_pedido.is_valid():
            novo_pedido.save()
            return redirect("pagina_inicial")
    else:
        novo_pedido = formularioPedido()
    return render(request, "cadastroPedido.html", {"formulario": novo_pedido, "pedidos": busca_pedido})
