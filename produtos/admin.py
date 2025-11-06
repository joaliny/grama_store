from django.contrib import admin
from .models import Grama

@admin.register(Grama)
class GramaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'preco_por_m2', 'disponivel', 'data_cadastro']
    list_filter = ['tipo', 'disponivel', 'data_cadastro']
    search_fields = ['nome', 'descricao']
    list_editable = ['preco_por_m2', 'disponivel']
    
    class Meta:
        verbose_name = 'Grama'
        verbose_name_plural = 'Gramas'