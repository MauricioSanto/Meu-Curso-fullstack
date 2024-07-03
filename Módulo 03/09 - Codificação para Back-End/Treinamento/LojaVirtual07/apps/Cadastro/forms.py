from django import forms
from .models import *

class FormularioCarros(forms.ModelForm):
    class Meta:
        model = carros
        fields = "__all__"
