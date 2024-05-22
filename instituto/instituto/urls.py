from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para la interfaz de administración de Django
    path('', include('alumnos.urls')),  # Incluye las rutas de la aplicación 'alumnos'
    path("accounts/", include("django.contrib.auth.urls")),  # Incluye las rutas de autenticación predeterminadas de Django
]

print("paso por urls de instituto")  # Imprime un mensaje de depuración cuando se cargan las URLs

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Añade configuración para servir archivos de medios durante el desarrollo
