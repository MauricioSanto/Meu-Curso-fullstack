from django.urls import path
from .views import *

urlpatterns = [
    path('lista-clientes', VerClientes, name= "pagina_Cliente"),
    path('index', VerIndex),
    path('login', VerLogin),
    path("",LinkInicial, name="pagina_index"),
    path("login", LinkLogin, name="pagina_login"),
    path("clientes", VerClientes, name="pagina_inicial"),
    path("ver_cliente/<int:id_cliente>/", DetalhesCliente, name="detalhes_clientes")

]
