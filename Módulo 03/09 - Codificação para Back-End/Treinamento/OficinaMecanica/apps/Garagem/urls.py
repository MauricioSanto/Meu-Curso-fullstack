from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio),
    path('cliente/',VerClientes ),
    path('veiculos/',VerVeiculos),
    path('mecanico/',VerMecanicos),
    path('OrdemServiço/',VerOrdemServico),
    path('peças/',VerPecas),
    path('vendas/',VerVendas)
]

