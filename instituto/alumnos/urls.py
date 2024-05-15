#from django.conf.urls import url
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin


urlpatterns = [
   #path('base', views.base, name='base'),
   path('', views.home, name='home'),
   path('nosotros', views.nosotros, name='nosotros'),
   path('contacto', views.contacto, name='contacto'),
   path('cursos', views.cursos, name='cursos'),
   path('conserje/', views.conserje, name='conserje'),
   path('visitas/', views.visitas, name='visitas'),
   path('bitacoras/', views.bitacoras, name='bitacoras'),
   
   # CRUD
   path('gestioncur', views.gestioncur, name='gestioncur'),
   path('nuevocur', views.nuevocur, name='nuevocur'),  
   path('editarcur/<codigo>', views.editarcur, name='editarcur'),
   path('borrarcur/<codigo>', views.borrarcurso, name='borrarcur'),   

   # GESTION USUARIOS
   #path('login', views.login, name='login'),
   path('salir', views.salir, name='salir'),
      
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
