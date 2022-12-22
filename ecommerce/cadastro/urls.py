
from django.urls import path

from . import views

urlpatterns = [
    path('', views.logar, name='login'),
    path('teste', views.teste, name='acesso'),
    path('cadastrar', views.cadastrar_usuario, name='cadastrar'),
    path('adicionais', views.cadastrar_adicionais, name='adicionais'),
    path('desejo/<int:produto_id>', views.addDesejos, name='desejo'),
    path('delDesejo/<int:id_desejo>', views.delDesejo, name='delDesejo')
]

