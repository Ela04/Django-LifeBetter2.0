#from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   #path('index', views.index, name='index'),
   #path('listadoSQL', views.listadoSQL, name='listadoSQL'),
   path('base', views.base, name='base'),  # Ruta para la vista 'base'
   path('', views.home, name='home'),  # Ruta para la vista 'home'
   path('nosotros', views.nosotros, name='nosotros'),  # Ruta para la vista 'nosotros'
   path('contacto', views.contacto, name='contacto'),  # Ruta para la vista 'contacto'
   path('cursos', views.cursos, name='cursos'),  # Ruta para la vista 'cursos'
   
   # CRUD
   path('gestioncur', views.gestioncur, name='gestioncur'),  # Ruta para la vista de gestión de cursos
   path('nuevocur', views.nuevocur, name='nuevocur'),  # Ruta para la vista de crear un nuevo curso
   path('editarcur/<codigo>', views.editarcur, name='editarcur'),  # Ruta para la vista de editar un curso
   path('borrarcur/<codigo>', views.borrarcurso, name='borrarcur'),  # Ruta para la vista de borrar un curso

   # GESTIÓN DE USUARIOS
   path('login', views.login, name='login'),  # Ruta para la vista de inicio de sesión
   path('salir', views.salir, name='salir'),  # Ruta para la vista de cerrar sesión
] 

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Añade la configuración para servir archivos de medios durante el desarrollo
