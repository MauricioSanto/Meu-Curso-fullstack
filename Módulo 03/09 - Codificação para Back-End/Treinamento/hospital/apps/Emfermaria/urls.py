from django.urls import path
from .views import *

urlpatterns = [
    path("", VerPacientes, name="pagina_inicial"),
    path("editar-paciente/<int:id_paciente>/", EditarPaciente, name="pg_editar_paciente"),

]

