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
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        verbose_name = "plato"
        verbose_name_plural = "platos"
        ordering = ['nombre']
        return self.nombre
