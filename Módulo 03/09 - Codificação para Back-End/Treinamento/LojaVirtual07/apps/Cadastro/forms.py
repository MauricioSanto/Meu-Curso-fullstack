from django import forms
from .models import *

class FormularioCarros(forms.ModelForm):
    class Meta:
        model = carros
        fields = "__all__"

class FormularioFuncionario(forms.ModelForm):
    class Meta:
        model =  cadastro_funcionarios
        fields = "__all__"
