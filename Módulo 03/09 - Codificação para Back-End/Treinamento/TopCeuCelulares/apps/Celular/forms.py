from django import forms
from .models import *


class FormularioCelular(forms.ModelForm):
    class Meta:
        model = celular
        fields = "__all__"
