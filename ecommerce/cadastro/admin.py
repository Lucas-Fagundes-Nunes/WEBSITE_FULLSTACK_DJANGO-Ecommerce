from django.contrib import admin

# Register your models here.
from .models import Adicionai, Desejo, Pedido, Usuarios


class DesejoAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'produto')
    list_display_links = ('id','user', 'produto')

class UusariosAdicionais(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'nascimento')
    list_display_links = ('id', 'user', 'cpf', 'nascimento')

admin.site.register(Usuarios)
admin.site.register(Adicionai, UusariosAdicionais)
admin.site.register(Desejo, DesejoAdmin)
admin.site.register(Pedido)