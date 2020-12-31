from django.contrib import admin
from .models import Categoria, Plato, Pedidos

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

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido_id', 'cliente', 'post_nombre', 'status')
    list_filter = ('pedido_id', 'cliente', 'status', 'nombre__nombre')
    ordering = ('pedido_id','cliente','status')

    def post_nombre(self, obj):
        return ", ".join([p.nombre for p in obj.nombre.all().order_by("nombre")])
    post_nombre.short_description = "Platos"
    
admin.site.register(Pedidos,PedidoAdmin)

