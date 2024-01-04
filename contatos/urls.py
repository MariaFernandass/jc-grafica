from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

app_name = "contatos"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('statuspedido/<int:id>', views.statuspedido, name='statuspedido'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('novo', views.novo, name='novo'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('administrador',views.administrador, name='administrador'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('remover/<int:id>', views.remover, name='remover')
]