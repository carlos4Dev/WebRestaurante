from django import forms
from .models import Categoria, Plato, Pedidos

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['categoria_id','nombre']
        widgets = {
            'categoria_id': forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Número de categoría'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'place-holder':'Nombre'}),
        }
        labels = {
            'categoria-id':'', 'nombre':''
        }

class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = ['plato_id','nombre', 'categoria_id', 'precio']
        widgets = {
            'plato_id': forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Número de plato'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'place-holder':'Nombre'}),
            'categoria_id': forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Número de categoría'}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Precio'}),
        }
        labels = {
            'plato_id':'', 'nombre':'Nombre', 'categoria_id':'Categoría','precio':'Precio'
        }

class PedidosForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ['pedido_id','cliente','nombre','status']
        widgets = {
            'pedido_id':forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Número de pedido'}),
            'cliente':forms.TextInput(attrs={'class':'form-control', 'place-holder':'Nombre'}),
            'nombre':forms.SelectMultiple(attrs={'class':'form-control','place-holder':'Platos'}),
            'status':forms.Select(attrs={'class':'form-control'})
        }
        labels = {
            'pedido_id':'Número pedido', 'cliente':'Nombre', 'nombre':'Plato', 'status':'Estado'
        }