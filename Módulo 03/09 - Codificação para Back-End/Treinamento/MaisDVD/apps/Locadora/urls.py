from django.urls import path
from .views import *

urlpatterns = [
    path('',Inicial, name= "pagina_index"),
    path("card", VerDvd, name="pagina_inicial"),
    path("ver_Dvd/<int:id_Dvd>/", DetalhesDvd, name="detalhes_Dvd"),
	path("cadastro", LinkCadastro, name="pagina_cadastro"),
    path("editar-Dvd/<int:id_Dvd>/", EditarDvd, name="pg_editar_Dvd")

]

