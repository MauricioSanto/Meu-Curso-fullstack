from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name='pagina_index'),
    path('clientes',CriarClientes,name='pagina_clientes' ),
    path('veiculos',CriarVeiculo,name='pagina_veiculos'),
    path('mecanico',CriarMecanico,name='pagina_mecanicos'),
    path('OrdemServiço',CriarOrdemServico,name='pagina_OrdemServiço'),
    path('peças',CriarPecas,name='pagina_pecas'),
    path('vendas',CriarVendas,name='pagina_vendas')
]

