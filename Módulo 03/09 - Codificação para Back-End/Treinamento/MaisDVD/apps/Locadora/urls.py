from django.urls import path
from .views import *

urlpatterns = [
    path("", VerDvd, name="pagina_inicial"),
    path("ver_Dvd/<int:id_Dvd>/", DetalhesDvd, name="detalhes_Dvd")

]
