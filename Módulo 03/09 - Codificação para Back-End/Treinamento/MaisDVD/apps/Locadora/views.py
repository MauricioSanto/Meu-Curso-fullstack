from django.shortcuts import render
from .models import *

def VerDvd(request):
    Dvd_lista = DVD.objects.all()
    return render(request, "lista-Dvd.html", {"Dvds": Dvd_lista})

def DetalhesDvd(request, id_Dvd):
    busca = DVD.objects.get(id=id_Dvd)
    return render(request, "detalhes_Dvd.html", {"Dvds": busca})


