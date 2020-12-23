from django.contrib import admin
from .models import Categoria, Plato

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria_id', 'nombre')
    ordering = ('categoria_id',)

admin.site.register(Categoria,CategoriaAdmin)

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('plato_id', 'nombre', 'categoria_id')
    list_filter = ('categoria_id', 'nombre')
    ordering = ('categoria_id','plato_id')

admin.site.register(Plato,PlatoAdmin)