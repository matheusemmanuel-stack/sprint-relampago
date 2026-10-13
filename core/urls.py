
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.listar_e_criar_projetos,
        name='listar_e_criar_projetos'
    ),

    path(
        'tarefas/',
        views.listar_e_criar_tarefas,
        name='listar_e_criar_tarefas'
    ),

    path(
        'projetos/<int:pk>/editar/',
        views.projeto_editar,
        name='projeto_editar'
    ),

    path(
        'projetos/<int:pk>/excluir/',
        views.projeto_excluir,
        name='projeto_excluir'
    ),

    path(
        'tarefas/<int:pk>/excluir/',
        views.tarefa_excluir,
        name='tarefa_excluir'
    ),
]