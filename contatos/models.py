from django.db import models

# Create your models here.
class Pedido(models.Model):
    produto = models.CharField(max_length=250)
    quantidade = models.IntegerField()
