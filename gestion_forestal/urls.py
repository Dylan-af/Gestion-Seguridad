"""
URL Configuration para gestion_forestal project.
"""
Sistema de Gestión de Seguridad Forestal
Configuración de URLs principales del proyecto
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('seguridad_app.urls')),  # Incluir URLs de la aplicación principal
]
