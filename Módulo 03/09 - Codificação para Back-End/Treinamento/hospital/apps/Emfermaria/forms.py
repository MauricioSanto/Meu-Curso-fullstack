from django import forms
from .models import *

class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
