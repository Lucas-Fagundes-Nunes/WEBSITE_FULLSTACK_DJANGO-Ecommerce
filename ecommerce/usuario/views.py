import os  # por causa do path

from django.conf import \
    settings  # Importa o o arquivo settings que contem tudo sobre o projeto (Base dirs)
from django.contrib.auth.decorators import \
    login_required  # Redireicionar caso não logado
from django.http import HttpResponse  # RESPOSTA ( NÃO NECESSARIO )
from django.shortcuts import render
from PIL import Image  # upload imagem
from projetoecommerce.models import Cor, Produto, Tamanho

# Create your views here.

@login_required # caso o usuário não esteja cadastrado
def dashboard(request):
    return render(request, 'dashboard/index.html')
 
@login_required
def addCor(request):
    if request.method == 'POST':      
        nomecor = request.POST.get('cor')
        addCor = Cor.objects.create(cor=nomecor)
        addCor.save()
        return render(request, 'dashboard/index.html')

@login_required
def addTamanho(request):
    if request.method == 'POST':
        newTamanho = request.POST.get('tamanho')
        newGrupo = request.POST.get('grupo')
        addTamanho = Tamanho.objects.create(tamanho=newTamanho, grupo=newGrupo)
        addTamanho.save()
        return render(request, 'dashboard/index.html')

@login_required
def addProduto(request):
    if request.method == 'POST':
            
        imagem = request.FILES.get('image')
        img = Image.open(imagem) # PIL imagem
        path = os.path.join(settings.BASE_DIR, f'media/imagens/{imagem}')
        img = img.save(path)



        nome = request.POST.get('nome')
        promo = request.POST.get('promocao')
        descricao = request.POST.get('descricao')
        especial = request.POST.get('especial')
        grupo = request.POST.get('grupo')
        valor = request.POST.get('valor')
        estoque = request.POST.get('estoque')
        valoranterior = request.POST.get('valoranterior')
        
        if especial == 'on':
            especial = True
        else: 
            especial = False
    
    
        addProduto = Produto.objects.create(image=imagem, nome=nome, promocao=promo, descricao=descricao, especiais=especial, grupoTamanho=grupo, valor=valor, estoque=estoque, valoranterior=valoranterior)
        addProduto.save()
        return render(request, 'dashboard/index.html')


