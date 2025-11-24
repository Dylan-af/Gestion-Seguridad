"""
URL Configuration para gestion_forestal project.
TI3041_Backend_Checklist - Evaluación N°3
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('seguridad_app.urls')),  # Incluir URLs de la aplicación principal
]
