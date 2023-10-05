from django.urls  import path
from . import views

app_name = "contatos"

urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.novo, name='novo'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('remover/<int:id>', views.remover, name='remover')
]