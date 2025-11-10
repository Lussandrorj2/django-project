from django.shortcuts import render 
def home(request): 
# 1. Crie seu dicionário de contexto 
    context = { 
        'nome_usuario': 'Júnior', 
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'] 
} 
# 2. Passe o 'context' como terceiro argumento do render() 
    return render(request, 'home.html', context) 