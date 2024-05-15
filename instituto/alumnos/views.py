
from django.shortcuts import render, redirect
from .models import Cursos, AreaCursos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CursosForm

# Create your views here.
#creación pagina conserje#
def conserje(request):
    return render(request, 'conserje/conserje.html')
#creación pagina visitas#  
def visitas(request):
    return render(request, 'conserje/visitas.html')
#creación pagina bitacoras#
def bitacoras(request):
    return render(request, 'conserje/bitacoras.html')

#def base(request):
#    return render(request, 'alumnos/base.html')

def home(request):
    return render(request, 'alumnos/home.html')
def nosotros(request):
    return render(request, 'alumnos/nosotros.html')
def contacto(request):
    return render(request, 'alumnos/contacto.html')
def cursos(request):
    cursos = Cursos.objects.all()
    context={"cursos":cursos}
    return render(request, 'alumnos/cursos.html', context)


## GESTION DE CURSOS
@login_required
def gestioncur(request):
    cursos = Cursos.objects.all()
    context={"cursos":cursos}
    return render(request, 'alumnos/gestion/gestioncur.html', context)


# CRUD
# https://www.youtube.com/watch?v=ezIj71CX944
def nuevocur(request):
    formulario = CursosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestioncur')
    return render(request, "alumnos/gestion/nuevocurso.html", {"formulario": formulario})

def editarcur(request, codigo):
    cursos = Cursos.objects.get(codigo=codigo)
    formulario = CursosForm(request.POST or None, request.FILES or None, instance=cursos)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestioncur')
    return render(request, "alumnos/gestion/editarcurso.html", {"formulario": formulario})

def borrarcurso(request, codigo):
    cursos = Cursos.objects.get(codigo=codigo)
    cursos.delete()
    messages.success(request, '¡Curso Eliminado!')
    return redirect('gestioncur')



#GESTION USUARIOS
def login(request):
    return render(request, "alumnos/login.html")

def salir(request):
    logout(request)
    return redirect('/')
