from django.shortcuts import render, redirect
from .models import *
from .forms import *


def VerCelular (request):
    celular_lista = celular.objects.all()
    return render(request, "index.html", {"celulares": celular_lista})

def DetalhesCelular(request, id_celular):
    busca = celular.objects.get(id=id_celular)
    return render(request, "detalhes_celulares.html", {"celulares": busca})

def CadastrarCelular(request):
    busca_Celular = celular.objects.all()
    if request.method == "POST":
        novo_celular = FormularioCelular(request.POST, request.FILES)
        if novo_celular.is_valid():
            novo_celular.save()
            return redirect("pagina_inicial")
    else:
        novo_celular = FormularioCelular()
    return render(request, "pagina_celular.html", {"formulario": novo_celular, "celulares": busca_Celular})

def EditarCelular(request, id_celular):
    busca_celular = celular.objects.get(id=id_celular)
    if request.method == "POST":
        celular_editado = FormularioCelular(request.POST, instance=busca_celular)
        if celular_editado.is_valid():
            celular_editado.save()
            return redirect('pagina_inicial')
    else:
        celular_editado = FormularioCelular(instance=busca_celular)
    return render(request, "editar_celular.html", {"formulario": celular_editado})






