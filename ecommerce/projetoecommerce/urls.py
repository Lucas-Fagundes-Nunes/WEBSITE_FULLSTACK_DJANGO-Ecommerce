from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewHome, name='home'),
    path('especiais', views.viewPromo, name='especial'),
    path('desejos', views.viewDesejos, name='desejo'),
    path('produto/<int:produto_id>', views.viewProduto, name='produto'),
    path('sacola', views.viewSacola, name='sacola'),
    path('cad', views.cadastroComentario, name='cad'),
    path('form', views.cadastroComentario, name='form'),
    path('addSacola', views.addSacola, name='addSacola'),
    path('delPedido/<int:id>', views.delProduto, name='delPedido')
] 

