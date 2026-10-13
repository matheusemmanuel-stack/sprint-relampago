
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.listar_e_criar_projetos,
        name='listar_e_criar_projetos'
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
]
