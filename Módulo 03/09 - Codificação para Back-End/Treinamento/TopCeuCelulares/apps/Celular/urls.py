from django.urls import path
from .views import *

urlpatterns = [
    path("", VerCelular, name="pagina_inicial"),
    path("ver_celular/<int:id_celular>/", DetalhesCelular, name="detalhes_celular"),
    path("celular",CadastrarCelular, name="pagina_Cadastro"),
    path("editar-celular/<int:id_celular>/", EditarCelular, name="pg_editar_celular"),
]



