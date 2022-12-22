from cadastro.models import Adicionai, Desejo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import Cor, Produto, Tamanho

# Create your views here.

def logar(request):
    request.session['nome'] = 'Lucas'
    print(request.session['nome'])

    return render(request, './usuarios/index.html', {})

def teste(request):
    request.session['nome']



# Cadastrar usuário
def cadastrar_usuario(request):
    if request.method == 'POST':
        try:
            usuario_aux = User.objects.get(email=request.POST['email'])
            if usuario_aux:
                return render(request, 'usuarios/cadastrar.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

        except User.DoesNotExist:
            nome = request.POST['nome']
            sobrenome = request.POST['sobrenome']
            username = request.POST['username']
            email = request.POST['email']
            senha = request.POST['senha']

            novoUsuario = User.objects.create_user(username=username, email=email, password=senha, first_name=nome ,last_name=sobrenome)
      
            novoUsuario.save()
            return render(request, 'usuarios/adicionais.html')
    else:
        return render(request, 'usuarios/cadastrar.html')


@login_required
def cadastrar_adicionais(request):
    verificar = Adicionai.objects.filter(user = request.user)
    if verificar:
        return redirect('/')
    else:
        if request.method == 'POST':
            cpf = request.POST['cpf']
            nascimento = request.POST['nascimento']
            cidade = request.POST['cidade']
            endereco = request.POST['endereco']
            numero = request.POST['numero']
                
            Adicional = Adicionai.objects.create(user=request.user,cpf=cpf, nascimento=nascimento, cidade=cidade, endereco=endereco, numero=numero)
            Adicional.save()
        
            return redirect('/')
        else:
            return render(request, 'usuarios/adicionais.html')
       

@login_required
def addDesejos(request,produto_id):
    validacaoUser = Desejo.objects.filter(user = request.user)
    validacaoProduto = Desejo.objects.filter(produto = produto_id)
    if validacaoUser and validacaoProduto:
        return redirect('/')
    else:
        id_produto = Produto.objects.get(id=produto_id)
        desejo = Desejo.objects.create(user=request.user, produto=id_produto)
        desejo.save()
    return redirect('desejo')


def delDesejo(request, id_desejo):
    desejo = Desejo.objects.get(id=id_desejo)
    desejo.delete()

    return redirect('desejo')


