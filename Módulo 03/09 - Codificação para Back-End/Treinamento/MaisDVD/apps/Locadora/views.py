from django.shortcuts import render, redirect
from .models import *
from .forms import *


def Inicial(request):
    return render(request, "index.html")

def VerDvd(request):
    Dvd_lista = DVD.objects.all()
    return render(request, "lista-Dvd.html")

def DetalhesDvd(request, id_Dvd):
    busca = DVD.objects.get(id=id_Dvd)
    return render(request, "detalhes_Dvd.html", {"Dvds": busca})

def LinkCadastro(request):
    return render(request, "cadastro.html")

def EditarDvd(request, id_Dvd):
    busca_Dvd = DVD.objects.get(id=id_Dvd)
    if request.method == "POST":
        Dvd_editado = FormularioDvd(request.POST, instance=busca_Dvd)
        if Dvd_editado.is_valid():
            Dvd_editado.save()
            return redirect('pagina_inicial')
    else:
        Dvd_editado = FormularioDvd()
    return render(request, "lista-Dvd.html", {"formulario": Dvd_editado})

