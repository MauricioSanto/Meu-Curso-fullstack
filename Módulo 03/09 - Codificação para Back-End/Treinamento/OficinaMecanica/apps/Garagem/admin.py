from django.contrib import admin
from .models import *


admin.site.register(Clientes)
admin.site.register(Veiculos)
admin.site.register(OrdemServico)
admin.site.register(Pecas)
admin.site.register(Mecanicos)
admin.site.register(Vendas)

# Register your models here.
