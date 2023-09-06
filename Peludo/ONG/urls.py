from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('mascotas/', views.mascotas,name='mascota'),
    path('contacto/', views.contacto,name='contacto'),
    
    path('agregarArticulo/', views.Add_Articulo),
    path('edicionArticulo/<codigo>', views.Edicion_Articulo),
    path('editarArticulo/', views.Edit_Articulo),
    path('eliminarArticulo/<codigo>', views.Del_Articulo)
]
