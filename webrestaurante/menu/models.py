from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True, verbose_name="Numero")
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['categoria_id']
        return self.nombre


class Plato(models.Model):
    plato_id = models.AutoField(primary_key=True, verbose_name="Numero")
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Plato")
    categoria_id = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE, verbose_name="Categoria")
    precio = models.IntegerField(blank=False, null=False, verbose_name="precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        verbose_name = "plato"
        verbose_name_plural = "platos"
        ordering = ['nombre']
        return self.nombre


EN_PROCESO = 'PROCESO'
ENTREGADO = 'ENTREGADO'
PAGADO = 'PAGADO'
STATUS_CHOICES = [
    {EN_PROCESO, 'En_proceso'},
    {ENTREGADO, 'Entregado'},
    {PAGADO, 'Pagado'},
]

class Pedidos(models.Model):
    pedido_id = models.AutoField(primary_key=True, verbose_name="Número pedido")
    cliente = models.CharField(max_length=100, verbose_name="Nombre cliente")
    nombre = models.ManyToManyField(Plato, verbose_name="Platos", related_name="get_pedidos")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=EN_PROCESO)

    def __str__(self):
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ['nombre']
        return self.cliente
 
