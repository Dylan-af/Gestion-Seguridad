"""
Sistema de Gestión de Seguridad Forestal
Configuración de URLs para la aplicación de seguridad

Incluye rutas protegidas para las operaciones CRUD
"""

from django.urls import path
from . import views

urlpatterns = [
    # Rutas de autenticación
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard (ruta protegida)
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # CRUD de Checklists (rutas protegidas)
    path('checklists/', views.checklist_list_view, name='checklist_list'),
    path('checklists/crear/', views.checklist_create_view, name='checklist_create'),
    path('checklists/<int:pk>/', views.checklist_detail_view, name='checklist_detail'),
    path('checklists/<int:pk>/editar/', views.checklist_edit_view, name='checklist_edit'),
    path('checklists/<int:pk>/eliminar/', views.checklist_delete_view, name='checklist_delete'),
    
    # CRUD de Visitas (rutas protegidas)
    path('visitas/', views.visita_list_view, name='visita_list'),
    path('visitas/crear/', views.visita_create_view, name='visita_create'),
    path('visitas/<int:pk>/', views.visita_detail_view, name='visita_detail'),
    path('visitas/<int:pk>/editar/', views.visita_edit_view, name='visita_edit'),
    path('visitas/<int:pk>/eliminar/', views.visita_delete_view, name='visita_delete'),
]
