from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa 
from .forms import TarefaForm  # 1. Importe o Model Tarefa 
def home(request): 
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm()
# 2. Use o ORM para buscar os dados! 
# Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa" 
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')
# 3. Atualize o contexto 
    context = { 
               
        'nome_usuario': 'Lussandro', 
        'tecnologias': ['Python', 'Django', 'Models', 'Admin'], 
        'tarefas': todas_as_tarefas,
        'form': form,
}# 4. Adicione as tarefas ao contexto 
    return render(request, 'home.html', context) 

def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.concluida = True  
        tarefa.save()
        return redirect('home')
    
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')
    