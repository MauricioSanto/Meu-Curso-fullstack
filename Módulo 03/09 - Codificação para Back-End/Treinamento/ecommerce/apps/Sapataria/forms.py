from django import forms
from .models import *


class formularioCliente(forms.ModelForm):
    class Meta:
        models = Cliente
        fields = "__all__"

class formularioSapato(forms.ModelForm):
    class Meta:
        models = Sapato
        fields = "__all__"

class formularioPedido(forms.ModelForm):
    class Meta:
        models = Pedido
        fields = "__all__"