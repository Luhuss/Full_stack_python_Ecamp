from django import forms 
from .models import Producto, Fabrica

class FabricaForm(forms.ModelForm):
    class Meta:
        model = Fabrica
        fields = ['nombre', 'pais']
        labels = {
            'nombre': 'Nombre del producto',
            'pais': 'País'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'})
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'fabrica']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'descripcion': 'Descripcion del producto',
            'fabrica': 'Fabrica del producto'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder':'Describe brevemente el producto...',}),
            'fabrica': forms.Select(attrs={'class': 'form-control'})
        }
            
