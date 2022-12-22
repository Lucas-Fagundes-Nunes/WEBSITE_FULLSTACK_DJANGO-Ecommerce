from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard),
    path('addCor', views.addCor, name='addCor'),
    path('addTamanho', views.addTamanho, name='addtamanho'),
    path('addProduto', views.addProduto, name='addProduto')
]
