from cadastro.models import Desejo, Pedido
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import Avaliacao, Cor, Produto, Tamanho

# Create your views here.

def viewHome(request):
    desejo = Desejo.objects.all().filter(user=request.user)
    produto = Produto.objects.all()

    return render(request, 'paginas/index.html', {'produto': produto, 'desejo':desejo})


def viewPromo(request):
    desejo = Desejo.objects.all().filter(user=request.user)
    promocoes = Produto.objects.all()
    return render(request, 'paginas/promocoes.html', {'promocao': promocoes, 'desejo':desejo})



@login_required
def viewDesejos(request):
    desejo = Desejo.objects.all().filter(user=request.user)
    produto = Produto.objects.all()
    return render(request, 'paginas/desejos.html', {'produto':produto, 'desejo':desejo})




def viewProduto(request, produto_id):
    id_produto = Produto.objects.get(id=produto_id)
    avaliacao = Avaliacao.objects.filter(id_produto = id_produto.id)
    cores = Cor.objects.all()
    tamanhos = Tamanho.objects.all()
  

    if request.method == 'POST':
        nome = request.POST.get('nome')
        comentario = request.POST.get('comentario')
        star = request.POST.get('star')

        newComentario = Avaliacao.objects.create(nome=nome,avaliacao=comentario,star=star,id_produto=id_produto)

    return render(request, 'paginas/produto.html', {'produto':id_produto, 'avaliacoes':avaliacao, 'cores': cores, 'tamanhos': tamanhos})





@login_required
def viewSacola(request):
    pedidoUm = Pedido.objects.all().filter(user=request.user)
    total = 0
    for p in pedidoUm:
        produto = Produto.objects.all().filter(nome=p.produto)
        for v in produto:
            total += v.valor

    pedido = Pedido.objects.all().filter(user=request.user)
    produto = Produto.objects.all()
    
    return render(request, 'paginas/sacola.html', {'produto':produto, 'pedido':pedido, 'total': total})
    


@login_required
def addSacola(request):
    if request.method == 'POST':
        tamanho = request.POST['tamanho']
        cor = request.POST['cor']
        produto = request.POST['produto']

    # Validar se já tme ou não o pedido
        t = Tamanho.objects.get(id=tamanho)
        c = Cor.objects.get(id=cor)
        p = Produto.objects.get(id=produto)
        adicionar = Pedido.objects.create(user=request.user,tamanho=t, cor=c, produto=p) 
        adicionar.save()
        return redirect('sacola')
    return redirect('')


@login_required
def delProduto(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect('sacola')
    



def cadastroComentario(request):
    if request.method !='POST':
        return render(request, 'paginas/formulario.html')
    nome = request.POST.get('nome')
    #avaliacao = request.POST.get('avaliacao')
    #star = request.POST.get('star')

    if not nome:

        return render(request, 'paginas/index.html')
    


    # DELETE
    #delete = Cor.objects.get(id=7)
    #delete.delete()

    # UPDATE
    #update = Cor.objects.get(id=7)
    #update.cor=nome
    #update.save()

    # CREATE
    #cadastrar = Cor.objects.update(cor=nome)
    #cadastrar.save()

    return render(request, 'paginas/formulario.html')
