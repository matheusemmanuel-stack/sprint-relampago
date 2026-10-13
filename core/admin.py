
from django.contrib import admin
from .models import Projeto, Tarefa


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio')
    search_fields = ('nome', 'descricao')
    ordering = ('-data_inicio',)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridade', 'concluido', 'projeto')
    list_filter = ('prioridade', 'concluido')
    search_fields = ('titulo', 'projeto__nome')
    list_editable = ('concluido',)
    list_select_related = ('projeto',)