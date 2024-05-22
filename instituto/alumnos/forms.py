# CREAR CLASES PARA FORMULARIOS
from django.forms import ModelForm
from django import forms
from .models import Cursos

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos  # Especifica el modelo 'Cursos' para el formulario
        fields = ['codigo', 'nombre', 'sence','fecha_creacion', 'id_Area', 'modalidad', 'objetivo', 'horas','activo', 'img'] 
        # Lista de campos específicos del modelo que se incluirán en el formulario (comentado)
        
        fields = '__all__'  # Incluirá todos los campos del modelo 'Cursos' en el formulario
