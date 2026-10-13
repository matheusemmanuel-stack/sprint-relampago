from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm


def listar_e_criar_projetos(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_e_criar_projetos')
    else:
        form = ProjetoForm()

    projetos = Projeto.objects.all().order_by('-data_inicio')

    return render(request, 'core/listar_e_criar.html', {
        'form': form,
        'projetos': projetos,
    })