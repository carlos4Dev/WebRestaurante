from django.shortcuts import render
from .models import Categoria, Plato

# Create your views here.
def menu(request):
    categorias = Categoria.objects.all()
    platos = Plato.objects.all()
    return render(request, "menu/menu.html", {'categorias':categorias, 'platos':platos})


