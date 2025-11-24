"""
Sistema de Gestión de Seguridad Forestal
Vistas y Controladores para Checklists y Visitas

Incluye:
- Gestión de sesiones y autenticación
- CRUD para Checklist
- CRUD para Visita
- Rutas protegidas con decoradores
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Checklist, Visita
from datetime import datetime


# ===========================
# VISTAS DE AUTENTICACIÓN
# ===========================

def login_view(request):
    """
    Vista para iniciar sesión
    Implementa hashing de contraseñas mediante el sistema de autenticación de Django
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.get_full_name() or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    """
    Vista para cerrar sesión
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')


# ===========================
# VISTA DASHBOARD
# ===========================

@login_required
def dashboard_view(request):
    """
    Vista principal del dashboard
    Muestra resumen de checklists y visitas
    """
    # Estadísticas de checklists
    total_checklists = Checklist.objects.count()
    checklists_pendientes = Checklist.objects.filter(estado='pendiente').count()
    checklists_completados = Checklist.objects.filter(estado='completado').count()
    
    # Estadísticas de visitas
    total_visitas = Visita.objects.count()
    visitas_criticas = Visita.objects.filter(resultado='critico').count()
    visitas_seguimiento = Visita.objects.filter(requiere_seguimiento=True).count()
    
    # Checklists recientes
    checklists_recientes = Checklist.objects.all()[:5]
    
    # Visitas recientes
    visitas_recientes = Visita.objects.all()[:5]
    
    context = {
        'total_checklists': total_checklists,
        'checklists_pendientes': checklists_pendientes,
        'checklists_completados': checklists_completados,
        'total_visitas': total_visitas,
        'visitas_criticas': visitas_criticas,
        'visitas_seguimiento': visitas_seguimiento,
        'checklists_recientes': checklists_recientes,
        'visitas_recientes': visitas_recientes,
    }
    
    return render(request, 'dashboard.html', context)


# ===========================
# CRUD DE CHECKLISTS
# ===========================

@login_required
def checklist_list_view(request):
    """
    Vista para listar todos los checklists
    """
    # Búsqueda y filtrado
    query = request.GET.get('q', '')
    estado_filter = request.GET.get('estado', '')
    
    checklists = Checklist.objects.all()
    
    if query:
        checklists = checklists.filter(
            Q(titulo__icontains=query) | 
            Q(area__icontains=query) |
            Q(descripcion__icontains=query)
        )
    
    if estado_filter:
        checklists = checklists.filter(estado=estado_filter)
    
    context = {
        'checklists': checklists,
        'query': query,
        'estado_filter': estado_filter,
    }
    
    return render(request, 'checklist_list.html', context)


@login_required
def checklist_create_view(request):
    """
    Vista para crear un nuevo checklist
    """
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        area = request.POST.get('area')
        estado = request.POST.get('estado')
        prioridad = request.POST.get('prioridad')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        observaciones = request.POST.get('observaciones', '')
        
        checklist = Checklist.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            area=area,
            responsable=request.user,
            estado=estado,
            prioridad=prioridad,
            fecha_vencimiento=fecha_vencimiento,
            observaciones=observaciones
        )
        
        messages.success(request, f'Checklist "{checklist.titulo}" creado exitosamente.')
        return redirect('checklist_list')
    
    context = {
        'estado_choices': Checklist.ESTADO_CHOICES,
        'prioridad_choices': Checklist.PRIORIDAD_CHOICES,
    }
    
    return render(request, 'checklist_form.html', context)


@login_required
def checklist_edit_view(request, pk):
    """
    Vista para editar un checklist existente
    """
    checklist = get_object_or_404(Checklist, pk=pk)
    
    if request.method == 'POST':
        checklist.titulo = request.POST.get('titulo')
        checklist.descripcion = request.POST.get('descripcion')
        checklist.area = request.POST.get('area')
        checklist.estado = request.POST.get('estado')
        checklist.prioridad = request.POST.get('prioridad')
        checklist.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        checklist.observaciones = request.POST.get('observaciones', '')
        
        checklist.save()
        
        messages.success(request, f'Checklist "{checklist.titulo}" actualizado exitosamente.')
        return redirect('checklist_list')
    
    context = {
        'checklist': checklist,
        'estado_choices': Checklist.ESTADO_CHOICES,
        'prioridad_choices': Checklist.PRIORIDAD_CHOICES,
        'is_edit': True,
    }
    
    return render(request, 'checklist_form.html', context)


@login_required
def checklist_delete_view(request, pk):
    """
    Vista para eliminar un checklist
    """
    checklist = get_object_or_404(Checklist, pk=pk)
    
    if request.method == 'POST':
        titulo = checklist.titulo
        checklist.delete()
        messages.success(request, f'Checklist "{titulo}" eliminado exitosamente.')
        return redirect('checklist_list')
    
    context = {
        'checklist': checklist,
    }
    
    return render(request, 'checklist_confirm_delete.html', context)


@login_required
def checklist_detail_view(request, pk):
    """
    Vista para ver detalles de un checklist
    """
    checklist = get_object_or_404(Checklist, pk=pk)
    visitas = checklist.visitas.all()
    
    context = {
        'checklist': checklist,
        'visitas': visitas,
    }
    
    return render(request, 'checklist_detail.html', context)


# ===========================
# CRUD DE VISITAS
# ===========================

@login_required
def visita_list_view(request):
    """
    Vista para listar todas las visitas
    """
    # Búsqueda y filtrado
    query = request.GET.get('q', '')
    tipo_filter = request.GET.get('tipo', '')
    resultado_filter = request.GET.get('resultado', '')
    
    visitas = Visita.objects.all()
    
    if query:
        visitas = visitas.filter(
            Q(codigo_visita__icontains=query) | 
            Q(lugar__icontains=query) |
            Q(hallazgos__icontains=query)
        )
    
    if tipo_filter:
        visitas = visitas.filter(tipo_visita=tipo_filter)
    
    if resultado_filter:
        visitas = visitas.filter(resultado=resultado_filter)
    
    context = {
        'visitas': visitas,
        'query': query,
        'tipo_filter': tipo_filter,
        'resultado_filter': resultado_filter,
    }
    
    return render(request, 'visita_list.html', context)


@login_required
def visita_create_view(request):
    """
    Vista para crear una nueva visita
    """
    if request.method == 'POST':
        codigo_visita = request.POST.get('codigo_visita')
        tipo_visita = request.POST.get('tipo_visita')
        fecha_visita = request.POST.get('fecha_visita')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')
        lugar = request.POST.get('lugar')
        checklist_id = request.POST.get('checklist')
        hallazgos = request.POST.get('hallazgos')
        resultado = request.POST.get('resultado')
        recomendaciones = request.POST.get('recomendaciones')
        requiere_seguimiento = request.POST.get('requiere_seguimiento') == 'on'
        
        checklist = None
        if checklist_id:
            checklist = Checklist.objects.get(pk=checklist_id)
        
        visita = Visita.objects.create(
            codigo_visita=codigo_visita,
            tipo_visita=tipo_visita,
            fecha_visita=fecha_visita,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            lugar=lugar,
            inspector=request.user,
            checklist=checklist,
            hallazgos=hallazgos,
            resultado=resultado,
            recomendaciones=recomendaciones,
            requiere_seguimiento=requiere_seguimiento
        )
        
        messages.success(request, f'Visita "{visita.codigo_visita}" creada exitosamente.')
        return redirect('visita_list')
    
    checklists = Checklist.objects.all()
    
    context = {
        'tipo_choices': Visita.TIPO_CHOICES,
        'resultado_choices': Visita.RESULTADO_CHOICES,
        'checklists': checklists,
    }
    
    return render(request, 'visita_form.html', context)


@login_required
def visita_edit_view(request, pk):
    """
    Vista para editar una visita existente
    """
    visita = get_object_or_404(Visita, pk=pk)
    
    if request.method == 'POST':
        visita.codigo_visita = request.POST.get('codigo_visita')
        visita.tipo_visita = request.POST.get('tipo_visita')
        visita.fecha_visita = request.POST.get('fecha_visita')
        visita.hora_inicio = request.POST.get('hora_inicio')
        visita.hora_fin = request.POST.get('hora_fin')
        visita.lugar = request.POST.get('lugar')
        
        checklist_id = request.POST.get('checklist')
        if checklist_id:
            visita.checklist = Checklist.objects.get(pk=checklist_id)
        else:
            visita.checklist = None
        
        visita.hallazgos = request.POST.get('hallazgos')
        visita.resultado = request.POST.get('resultado')
        visita.recomendaciones = request.POST.get('recomendaciones')
        visita.requiere_seguimiento = request.POST.get('requiere_seguimiento') == 'on'
        
        visita.save()
        
        messages.success(request, f'Visita "{visita.codigo_visita}" actualizada exitosamente.')
        return redirect('visita_list')
    
    checklists = Checklist.objects.all()
    
    context = {
        'visita': visita,
        'tipo_choices': Visita.TIPO_CHOICES,
        'resultado_choices': Visita.RESULTADO_CHOICES,
        'checklists': checklists,
        'is_edit': True,
    }
    
    return render(request, 'visita_form.html', context)


@login_required
def visita_delete_view(request, pk):
    """
    Vista para eliminar una visita
    """
    visita = get_object_or_404(Visita, pk=pk)
    
    if request.method == 'POST':
        codigo = visita.codigo_visita
        visita.delete()
        messages.success(request, f'Visita "{codigo}" eliminada exitosamente.')
        return redirect('visita_list')
    
    context = {
        'visita': visita,
    }
    
    return render(request, 'visita_confirm_delete.html', context)


@login_required
def visita_detail_view(request, pk):
    """
    Vista para ver detalles de una visita
    """
    visita = get_object_or_404(Visita, pk=pk)
    
    context = {
        'visita': visita,
    }
    
    return render(request, 'visita_detail.html', context)
