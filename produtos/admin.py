from django.contrib import admin
from .models import Produto, Categoria

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria', 'quantidade', 'codigo')
    list_display_links = ('id', 'nome', 'codigo')
    search_fields = ('id', 'nome', 'codigo')
    list_editable = ( 'preco', 'quantidade')
    list_filter = ['categoria']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
