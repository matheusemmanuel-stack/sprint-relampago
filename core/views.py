
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm


def listar_e_criar_projetos(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('listar_e_criar_projetos')
    else:
        form = ProjetoForm()

    projetos = Projeto.objects.all().order_by('-data_inicio')

    return render(request, 'core/listar_e_criar.html', {
        'form': form,
        'projetos': projetos,
    })


def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('listar_e_criar_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    projetos = Projeto.objects.all().order_by('-data_inicio')

    return render(request, 'core/listar_e_criar.html', {
        'form': form,
        'projeto': projeto,
        'projetos': projetos,
    })


def projeto_excluir(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('listar_e_criar_projetos')

    return render(
        request,
        'core/projeto_confirmar_exclusao.html',
        {'projeto': projeto}
    )


def listar_e_criar_tarefas(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('listar_e_criar_tarefas')
    else:
        form = TarefaForm()

    tarefas = Tarefa.objects.select_related('projeto').all()

    return render(request, 'core/listar_e_criar_tarefas.html', {
        'form': form,
        'tarefas': tarefas,
    })


def tarefa_excluir(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_e_criar_tarefas')

    return render(
        request,
        'core/confirmar_exclusao_tarefa.html',
        {'tarefa': tarefa}
    )