from django.shortcuts import render, redirect
from .models import Pedido
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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

@login_required
def novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        produto = request.POST.get('produto')
        tamanho = request.POST.get('tamanho')
        entrega = request.POST.get('entrega')
        foto = request.FILES['foto']

        fs = FileSystemStorage()
        filename = fs.save(foto.name, foto)

        # Obtenha o caminho da imagem
        foto_path = fs.url(filename)
        quantidade = int(request.POST.get('quantidade', 0))
        precos = {'Impressão preto e branco': 1, 'Impressão colorida': 2, 'Impressão em papel fotográfico': 3, 'Impressão em papel adesivo': 4}
        preco_unitario = precos.get(produto, 0)
        novo_pedido = Pedido(nome=nome, email=email, produto=produto, tamanho=tamanho, entrega=entrega, quantidade=quantidade, foto=foto_path, preco_unitario=preco_unitario)
        novo_pedido.save()
        messages.success(request, 'Pedido criado com sucesso!')
        return redirect('dashboard')

    return render(request, 'novo.html')
@login_required
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
    ctx = {'c': pedido}

    if request.method == 'POST':
        produto = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade', 0))
        tamanho = request.POST.get('tamanho')
        entrega = request.POST.get('entrega')
        precos = {'Impressão preto e branco': 1, 'Impressão colorida': 2, 'Impressão em papel fotográfico': 3, 'Impressão em papel adesivo': 4}

        pedido.produto = produto
        pedido.quantidade = quantidade
        pedido.tamanho = tamanho
        pedido.entrega = entrega
        pedido.preco_unitario = precos.get(produto, 0)
        
        pedido.save()

        messages.success(request, 'Pedido atualizado com sucesso!')
        return redirect('dashboard')
    else:
        return render(request, 'editar.html', ctx)

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

@login_required
def dashboard(request):
    lista = Pedido.objects.filter(email=request.user.email)
    soma_total = sum(pedido.calcular_preco_total() for pedido in lista)
    return render(request, 'dashboard.html', {'lista': lista, 'soma_total': soma_total})
    
#administrador
def administrador(request):
    if request.user.is_staff:
        lista = Pedido.objects.all()
        return render(request, 'administrador.html', {'lista': lista},);
    elif request.user.is_authenticated:
        messages.error(request,"Acesso negado, você não tem permissão de administrador")
        return redirect('dashboard')
    else:
        messages.error(request,"Permissão negada")
        return redirect('index') 
    
def statuspedido(request, id):
    if request.user.is_staff:
        pedido = Pedido.objects.get(pk=id)
        ctx = {'c': pedido}

        if request.method == 'POST':
            status = request.POST.get('status')
            pedido.status = status
            pedido.save()
            messages.success(request, 'Pedido atualizado com sucesso!')
            return redirect('administrador')
        else:
            return render(request, 'statuspedido.html', ctx)
    else:
        messages.error(request,"Permissão negada")
        return redirect('index') 