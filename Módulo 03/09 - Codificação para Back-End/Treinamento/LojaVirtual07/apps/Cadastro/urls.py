from django.urls import path
from .views import *

urlpatterns = [
    	
    path("", LinkInicial, name="pagina_index"),
    path('', VerFuncionario),
	path("Funcionarios", LinkCadastroFuncionario, name="pagina_Funcionarios"),
    path("Clientes", LinkClientes, name="pagina_Clientes" ),
    path("Carros", Linkcarros, name="pagina_Carros" ),
    path("pagamento", Linkpagamento, name="pagina_Pagamento" ),
    path("pedidos",PedidosCarros,name="pagina_pedidos"),
    path("ver_carro/<int:id_carro>/", DetalhesCarro, name="detalhes_carros")
]
