from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Pedido
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        #Validações
        if not email.strip():
            messages.warning(request,'Preencha o campo do email')
            return redirect('login')
        if not senha.strip():
            messages.warning(request,'Preencha o campo da senha')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            #autenticação do django
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request,'Login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request,'Senha incorreta')
            return redirect('login')
        else:
            messages.error(request,'Email incorreto')
            return redirect('login')
    else:
        return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def novo(request):
    if request.POST:
        p = request.POST.get('produto')
        q = request.POST.get('quantidade')
        novo = Pedido(produto = p, quantidade = q)
        novo.save()
        return redirect('dashboard')
    else:
        return render(request, 'novo.html')


def remover(request, id):
    pedido = Pedido.objects.get(pk=id)
    if pedido != None:
        pedido.delete()
        messages.success(request, "Objeto removido com sucesso")    
    else:
        messages.error(request, "Objeto não encontrado")
    
    return redirect('dashboard')

def editar(request, id):
    pedido = Pedido.objects.get(pk=id)
    ctx = {
        'c': pedido
    }
    if request.POST:
        p = request.POST.get("produto")
        q = request.POST.get("quantidade")
        pedido.produto = p
        pedido.quantidade = q
        pedido.save()
        return redirect('dashboard')
    else:
        return render(request, "editar.html", ctx)

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        #Validações    
        if not nome.strip(): 
            print('O campo precisa ser preenchido')
            return redirect('cadastro')
        if not email.strip():
            print('O campo precisa ser preenchido')
            return redirect('cadastro')
        if not senha.strip():
            print('O campo precisa ser preenchido')
            return redirect('cadastro') 
        if not senha2.strip():
            print('O campo precisa ser preenchido')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request,'ATENÇÃO, As senhas estão diferentes.')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'ATENÇÃO, Já existe um usuario cadastrado com esse email.')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request,'Você foi cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        ctx = {
        'lista' : Pedido.objects.all()
        }
        return render(request, 'dashboard.html', ctx)
    else:
        return render('index')