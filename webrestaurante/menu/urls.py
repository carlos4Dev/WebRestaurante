from django.urls import path
from .views import CategoriaListView, CategoriaDetailView, CategoriaCreate, CategoriaUpdate, CategoriaDelete, PlatoListView, PlatoDetailView, PlatoCreate, PlatoUpdate, PlatoDelete

from . import views

urlpatterns = [
    path('', views.menu, name="menu"),
]

menu_patterns = ([
    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('<int:pk>/<slug:slug>/', CategoriaDetailView.as_view(), name='categoria'),
    path('createCategoria/', CategoriaCreate.as_view(), name='createCategoria'),
    path('updateCategoria/<int:pk>/', CategoriaUpdate.as_view(), name='updateCategoria'),
    path('deleteCategoria/<int:pk>/', CategoriaDelete.as_view(), name='deleteCategoria'),
    path('platos/', PlatoListView.as_view(), name='platos'),
    path('<int:pk>/<slug:slug>/', PlatoDetailView.as_view(), name='plato'),
    path('createPlato/', PlatoCreate.as_view(), name='createPlato'),
    path('updatePlato/<int:pk>/', PlatoUpdate.as_view(), name='updatePlato'),
    path('deletePlato/<int:pk>/', PlatoDelete.as_view(), name='deletePlato')
], 'menu')