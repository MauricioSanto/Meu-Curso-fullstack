from django.urls import path
from .views import *

urlpatterns = [
    path("", LinkInicial, name="pagina_index"),
    path("cadastro", CriarCarros, name="pagina_cadastro"),
	path("Funcionarios", LinkCadastroFuncionario, name="pagina_Funcionarios"),
    path("Clientes", LinkClientes, name="pagina_Clientes" ),
    path("Carros", Linkcarros, name="pagina_Carros" ),
    path("pagamento", Linkpagamento, name="pagina_Pagamento" ),
    path("pedidos",PedidosCarros,name="pagina_pedidos"),
    path("ver_carro/<int:id_carro>/", DetalhesCarro, name="detalhes_carros"),
    path("deleteCarros",VerCarros, name= "delete_carros"),
    path("excluir-carro/<int:id_carro>", ExcluirCarro, name="conf_excluir_carro"),
    path("editarCarro", VerCarros, name="pagina_editar"),
    path("editar-carro/<int:id_carro>/", EditarCarro, name="pg_editar_carro"),
    path("cadastroFuncionario",CriarFuncionario,name="pagina_cadastro_funcionario"),
    path("deleteFuncionario",VerFuncionario, name='delete_funcionario'),
    path("excluir-funcionario/<int:id_funcionario>",ExcluirFuncionario,name="pagina_delete_funcionario"),
]


