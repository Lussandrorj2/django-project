from django.shortcuts import render 
from .models import Tarefa  # 1. Importe o Model Tarefa 
def home(request): 
# 2. Use o ORM para buscar os dados! 
# Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa" 
    todas_as_tarefas = Tarefa.objects.all() 
# 3. Atualize o contexto 
    context = { 

        'nome_usuario': 'Lussandro', 
        'tecnologias': ['Python', 'Django', 'Models', 'Admin'], 
        'tarefas': todas_as_tarefas 
}# 4. Adicione as tarefas ao contexto 
    return render(request, 'home.html', context) 