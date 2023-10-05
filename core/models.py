from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Importe o modelo User padrão do Django

class Alimentos(models.Model):
    # Campos do seu modelo de entidade
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    # ...
    calorias = models.FloatField(default=0.0)

    # Campo ForeignKey para relacionar com o usuário
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alimentos')

    def __str__(self):
        return self.nome
