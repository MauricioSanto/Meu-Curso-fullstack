from django.urls import path
from .views import *

urlpatterns = [
    path('lista-clientes', VerClientes),
    path('index', VerIndex),
    path('login', VerLogin),
    path("",LinkInicial, name="pagina_index"),
    path("login", LinkLogin, name="pagina_login")
]
