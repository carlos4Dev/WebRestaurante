from django import forms
from .models import Categoria, Plato

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
        fields = ['plato_id','nombre', 'categoria_id']
        widgets = {
            'plato_id': forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Número de plato'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'place-holder':'Nombre'}),
            'categoria_id': forms.NumberInput(attrs={'class':'form-control', 'place-holder':'Número de categoría'}),
        }
        labels = {
            'plato_id':'', 'nombre':'', 'categoria_id':''
        }