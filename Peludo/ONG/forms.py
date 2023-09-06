#CREAR CLASES PARA FORMULARIOS
from django.forms import ModelForm
from .models import Tb_Articulo

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']

class ArticuloForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']