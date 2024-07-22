from django import forms
from .models import *

class Autor_form(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ("__all__")

class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("__all__")

class Proveedor_form(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ("__all__")

class Producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("__all__")
