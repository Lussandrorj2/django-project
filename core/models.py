from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=200) 
# Um campo booleano (verdadeiro/falso), que por padrão é Falso 
    concluida = models.BooleanField(default=False) 
    
    criada_em = models.DateTimeField(auto_now_add=True) 
 
def __str__(self):
    return self.titulo
