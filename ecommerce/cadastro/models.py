from django.contrib.auth import get_user_model
from django.db import models
from projetoecommerce.models import Cor, Produto, Tamanho

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.IntegerField()
    senha = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Adicionai(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cpf = models.IntegerField()
    nascimento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()


class Desejo(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


class Pedido(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


