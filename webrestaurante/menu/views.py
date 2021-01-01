from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from .models import Categoria, Plato, Pedidos
from .forms import CategoriaForm, PlatoForm, PedidosForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class CategoriaListView(ListView):
    context_object_name = 'categoria_list'
    queryset = Categoria.objects.all()
    template_name = 'menu/categoria_list.html'

class CategoriaDetailView(DetailView):
    model = Categoria

@method_decorator(staff_member_required, name='dispatch')
class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('menu:categorias')

@method_decorator(staff_member_required, name='dispatch')
class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'menu/categoria_update_form.html'

    def get_success_url(self):
        return reverse_lazy('menu:updateCategoria', args=[self.object.categoria_id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('menu:categorias')


class PlatoListView(ListView):
    context_object_name = 'plato_list'
    queryset = Plato.objects.all()
    template_name = 'menu/plato_list.html'

class PlatoDetailView(DetailView):
    model = Plato

@method_decorator(staff_member_required, name='dispatch')
class PlatoCreate(CreateView):
    model = Plato
    form_class = PlatoForm
    success_url = reverse_lazy('menu:platos')

@method_decorator(staff_member_required, name='dispatch')
class PlatoUpdate(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('menu:updatePlato', args=[self.object.plato_id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PlatoDelete(DeleteView):
    model = Plato
    form_class = PlatoForm
    template_name = "menu/plato_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('menu:platos')

def menu(request):
    categorias = Categoria.objects.all()
    platos = Plato.objects.all()
    return render(request, "menu/menu.html", {'categorias':categorias, 'platos':platos})

def pedido(request):
    categorias = Categoria.objects.all()
    platos = Plato.objects.all()
    pedidos = Pedidos.objects.all()
    return render(request, "menu/pedido.html", {'categorias':categorias, 'platos':platos, 'pedidos':pedidos})

class PedidosListView(ListView):
    context_object_name = "pedido_list"
    queryset = Pedidos.objects.all()
    template_name = "menu/pedidos_list.html"

class PedidosDetailView(DetailView):
    model = Pedidos
 
class PedidosCreate(CreateView):
    model = Pedidos
    form_class = PedidosForm
    success_url = reverse_lazy('menu:pedidos')

class PedidosUpdate(UpdateView):
    model = Pedidos
    form_class = PedidosForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('menu:updatePedidos', args=[self.object.pedido_id]) + '?ok'    

@method_decorator(staff_member_required, name='dispatch')
class PedidosDelete(DeleteView):
    model = Pedidos
    form_class = PedidosForm
    template_name = "menu/pedido_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('menu:pedidos')