from django.shortcuts import render, redirect
from .models import Pedido
from django.contrib import messages
# Create your views here.
def index(request):
    ctx = {
        'lista' : Pedido.objects.all()
    }
    return render(request, 'index.html', ctx)

def novo(request):
    if request.POST:
        p = request.POST.get('produto')
        q = request.POST.get('quantidade')
        novo = Pedido(produto = p, quantidade = q)
        novo.save()
        return redirect('/contatos/')
    else:
        return render(request, 'novo.html')


def remover(request, id):
    pedido = Pedido.objects.get(pk=id)
    if pedido != None:
        pedido.delete()
        messages.success(request, "Objeto removido com sucesso")    
    else:
        messages.error(request, "Objeto não encontrado")
    
    return redirect('/contatos/')

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
        return redirect('/contatos/') 
    else:
        return render(request, "editar.html", ctx)


    