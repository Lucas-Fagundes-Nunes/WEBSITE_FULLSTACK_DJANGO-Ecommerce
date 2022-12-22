from django.db import models

# Create your models here.

class Cor(models.Model):
    cor = models.CharField(max_length=255)
    
    def __str__(self):
        return self.cor

class Tamanho(models.Model):
    tamanho = models.CharField(max_length=255)
    grupo = models.IntegerField()
    def __str__(self):
        return self.tamanho



class Produto(models.Model):
    image = models.ImageField(upload_to='imagens/')
    nome = models.CharField(max_length=255)
    promocao = models.CharField(max_length=50)
    descricao = models.TextField()
    especiais = models.BooleanField()
    grupoTamanho = models.IntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    valoranterior = models.CharField(max_length=255, null=True) 

    def __str__(self):
       return self.nome

       
class Avaliacao(models.Model):
    nome = models.CharField(max_length=255)
    avaliacao = models.TextField()
    star = models.IntegerField()
    id_produto = models.ForeignKey(Produto ,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
