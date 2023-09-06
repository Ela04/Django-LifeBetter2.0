from django.shortcuts import render, redirect
from .models import Tb_Articulo
from django.contrib import messages

# Create your views here.

# def home(request):
#     return render(request, "home.html")

def mascotas(request):
    return render(request, "mascotas.html")

def contacto(request):
    return render(request, "contacto.html")

def home(request):
     articuloListados = Tb_Articulo.objects.all()
     messages.success(request, '¡Articulos Listados!')
     return render(request, "gestionArticulos.html", {"articulos": articuloListados})

def Add_Articulo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    stock = request.POST['numStock']
    articulo = Tb_Articulo.objects.create(
        codigo=codigo, nombre=nombre, stock=stock)
    messages.success(request, '¡Artículo Registrado!')
    return redirect('/')

def Edit_Articulo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    stock = request.POST['numStock']
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    articulo.nombre = nombre
    articulo.creditos = stock
    articulo.save()
    messages.success(request, '¡Artículo Actualizado!')
    return redirect('/')

def Del_Articulo(request, codigo):
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    articulo.delete()
    messages.success(request, '¡Artículo Eliminado!')
    return redirect('/')

def Edicion_Articulo(request, codigo):
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    return render(request, "edicionArticulo.html", {"articulo": articulo})