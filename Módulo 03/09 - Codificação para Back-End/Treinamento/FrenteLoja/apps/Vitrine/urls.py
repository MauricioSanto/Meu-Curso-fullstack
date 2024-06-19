from django.urls import path
from .views import *

urlpatterns = [
    path("", VerProdutos, name="pagina_inicial"),
    path("ver_produto/<int:id_produto>/", DetalhesProduto, name="detalhes_produto")
]
