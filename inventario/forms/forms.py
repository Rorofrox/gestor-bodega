from django import forms
from inventario.models import Producto, Bodega, Movimiento, DetalleMovimiento, PerfilUsuario
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = PerfilUsuario
        fields = ('username', 'password1', 'password2', 'rol')

class DetalleMovimientoForm(forms.ModelForm):
    class Meta:
        model = DetalleMovimiento
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    bodega = forms.ModelChoiceField(queryset=Bodega.objects.all())
    cantidad = forms.IntegerField(initial=0)  # Agrega el campo de cantidad

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'bodega', 'cantidad')  # Incluye el campo de cantidad en los campos del formulario


class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ('bodega_origen', 'bodega_destino', 'productos',)