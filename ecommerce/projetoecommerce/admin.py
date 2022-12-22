from django.contrib import admin

from .models import Avaliacao, Cor, Produto, Tamanho

# Register your models here.


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('image','nome', 'valor')
    list_display_links = ('nome','valor')
    list_filter = ('nome', 'descricao')
    list_per_page = 40


admin.site.register(Cor)
admin.site.register(Tamanho)
admin.site.register(Avaliacao)
admin.site.register(Produto, ProdutoAdmin)
