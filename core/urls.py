from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.listar_e_criar_projetos, name='listar_e_criar_projetos'),
]