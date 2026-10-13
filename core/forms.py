from django import forms
from .models import Projeto


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio']
        labels = {
            'nome': 'Nome do Projeto',
            'descricao': 'Descrição',
            'data_inicio': 'Data de Início',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Ex: Sistema de Vendas',
                'required': True
            }),
            'descricao': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Descreva os objetivos do projeto...',
                'required': True
            }),
            'data_inicio': forms.DateInput(attrs={
                'type': 'date',
                'required': True
            }),
        }