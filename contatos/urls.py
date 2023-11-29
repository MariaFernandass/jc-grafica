from django.urls  import path
from . import views

app_name = "contatos"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('novo', views.novo, name='novo'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('remover/<int:id>', views.remover, name='remover')
]