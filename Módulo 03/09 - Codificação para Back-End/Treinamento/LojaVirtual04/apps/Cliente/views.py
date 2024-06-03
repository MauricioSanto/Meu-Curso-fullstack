from django.shortcuts import render
from .models import cliente

def Verclientes(request):
    clientes_lista = cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes_lista})


# Create your views here.
