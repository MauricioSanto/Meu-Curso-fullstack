from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name='pagina_index'),
    path('clientes',CriarClientes,name='pagina_clientes' ),
    path('veiculos',VerVeiculos,name='pagina_veiculos'),
    path('mecanico',VerMecanicos,name='pagina_mecanicos'),
    path('OrdemServiço',VerOrdemServico,name='pagina_OrdemServiço'),
    path('peças',VerPecas,name='pagina_pecas'),
    path('vendas',VerVendas,name='pagina_vendas')
]

