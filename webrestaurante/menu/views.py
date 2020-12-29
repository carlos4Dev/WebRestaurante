from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from .models import Categoria, Plato
from .forms import CategoriaForm, PlatoForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class CategoriaListView(ListView):
    model = Categoria

class CategoriaDetailView(DetailView):
    model = Categoria

@method_decorator(staff_member_required, name='dispatch')
class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('menu:menu')

@method_decorator(staff_member_required, name='dispatch')
class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('menu:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('menu:menu')



class PlatoListView(ListView):
    model = Plato

class PlatoDetailView(DetailView):
    model = Plato

@method_decorator(staff_member_required, name='dispatch')
class PlatoCreate(CreateView):
    model = Plato
    form_class = PlatoForm
    success_url = reverse_lazy('menu:menu')

@method_decorator(staff_member_required, name='dispatch')
class PlatoUpdate(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('menu:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PlatoDelete(DeleteView):
    model = Plato
    success_url = reverse_lazy('menu:menu')



def menu(request):
    categorias = Categoria.objects.all()
    platos = Plato.objects.all()
    return render(request, "menu/menu.html", {'categorias':categorias, 'platos':platos})


