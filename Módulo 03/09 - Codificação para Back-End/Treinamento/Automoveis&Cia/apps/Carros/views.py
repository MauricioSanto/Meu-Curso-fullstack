from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def automovel(request):
    return HttpResponse("carro do futuro")


def Vercarro(request):
    carros_lista = carro.objects.all()
    return render(request, 'index.html', {'carros': carros_lista})

