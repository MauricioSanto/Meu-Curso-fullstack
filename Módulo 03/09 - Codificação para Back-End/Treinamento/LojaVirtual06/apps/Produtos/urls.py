from django.urls import path
from .views import *

urlpatterns = [
    path('',VerProdutos),
    path("", LinkInicial, name="pagina_index"),
	path("cadastro", LinkCadastro, name="pagina_cadastro"),
]
