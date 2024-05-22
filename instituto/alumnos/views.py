from django.shortcuts import render, redirect
from .models import Cursos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CursosForm

# Crear tus vistas aquí

def base(request):
    return render(request, 'publico/base.html')

def home(request):
    return render(request, 'publico/home.html')

def nosotros(request):
    return render(request, 'publico/nosotros.html')

def contacto(request):
    return render(request, 'publico/contacto.html')

def cursos(request):
    cursos = Cursos.objects.all()
    context = {"cursos": cursos}
    return render(request, 'publico/cursos.html', context)


## GESTIÓN DE CURSOS
@login_required
def gestioncur(request):
    cursos = Cursos.objects.all()
    context = {"cursos": cursos}
    return render(request, 'gestion/gestioncur.html', context)


# CRUD (Crear, Leer, Actualizar, Eliminar)
def nuevocur(request):
    formulario = CursosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('gestioncur')
    return render(request, "gestion/nuevocurso.html", {"formulario": formulario})

def editarcur(request, codigo):
    cursos = Cursos.objects.get(codigo=codigo)
    formulario = CursosForm(request.POST or None, request.FILES or None, instance=cursos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('gestioncur')
    return render(request, "gestion/editarcurso.html", {"formulario": formulario})

def borrarcurso(request, codigo):
    cursos = Cursos.objects.get(codigo=codigo)
    cursos.delete()
    messages.success(request, '¡Curso Eliminado!')
    return redirect('gestioncur')


# GESTIÓN DE USUARIOS
def login(request):
    return render(request, "registration/login.html")

def salir(request):
    logout(request)
    return redirect("home")
