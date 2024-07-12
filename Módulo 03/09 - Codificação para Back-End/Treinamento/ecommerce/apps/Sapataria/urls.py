from django.urls import path
from .views import *
from .forms import *

urlpatterns = [
    path("",paginaindex, name="pagina_inicial"),
    path("cadastoCliente",CadastroCliente,name="pg_cadastro_cliente"),
    path("cadastroPedido", CadastroPedido, name="pg_cadastro_pedido"),
    path("CadastroSapato", CadastroSapato,name="pg_cadastro_sapato"),
]
