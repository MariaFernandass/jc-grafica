from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    nome = models.TextField(max_length=50, default="")
    email = models.TextField(max_length=50, default="") 
    produto = models.CharField(max_length=250)
    quantidade = models.IntegerField()
    tamanho = models.TextField(max_length=20, default="")
    foto = models.ImageField(upload_to="media/", blank=True, null=True)
    entrega = models.TextField(max_length=50, default="") 
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.TextField(max_length=10, default="Análise")

    def calcular_preco_total(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return self.produto