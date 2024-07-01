from django import forms
from .models import *

class FormularioClientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'email','celular','endereco']

class FormularioMecanico(forms.ModelForm):
    class Meta:
        model = Mecanicos
        fields = ['matricula', 'nome','especialidade','foto']

class FormularioOrdemServico(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['OrdemNumero', 'data','status','valor','pecas','veiculo']

class FormularioPecas(forms.ModelForm):
    class Meta:
        model = Pecas
        fields = '__all__'

class FormularioVeiculos(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = '__all__'

class FormularioVendas(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = '__all__'

