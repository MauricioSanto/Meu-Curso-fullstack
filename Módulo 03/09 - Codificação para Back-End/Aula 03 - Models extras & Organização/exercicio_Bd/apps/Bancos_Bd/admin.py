from django.contrib import admin

from .models import *

admin.site.register(Clientes)
admin.site.register(Produtos)
admin.site.register(Pedidos)
admin.site.register(Transportadora)
admin.site.register(Funcionario)

