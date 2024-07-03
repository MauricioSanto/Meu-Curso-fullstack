from django import forms
from .models import *

class FormularioDvd(forms.ModelForm):
    class Meta:
        model = DVD
        fields = '__all__'
