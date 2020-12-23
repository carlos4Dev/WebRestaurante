from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True, verbose_name="Numero")
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Categoria")

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    plato_id = models.AutoField(primary_key=True, verbose_name="Numero")
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Plato")
    categoria_id = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.nombre
