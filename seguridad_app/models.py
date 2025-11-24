"""
Modelos de datos para la aplicación seguridad_app
TI3041_Backend_Checklist - Evaluación N°3

Incluye dos entidades principales:
1. Checklist - Para registrar checklists operacionales
2. Visita - Para registrar visitas de seguridad
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Checklist(models.Model):
    """
    Modelo para gestionar Checklists Operacionales
    """
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    area = models.CharField(max_length=100, verbose_name="Área Forestal")
    responsable = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='checklists',
        verbose_name="Responsable"
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='pendiente',
        verbose_name="Estado"
    )
    prioridad = models.CharField(
        max_length=20, 
        choices=PRIORIDAD_CHOICES, 
        default='media',
        verbose_name="Prioridad"
    )
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        db_table = 'checklists'
        verbose_name = 'Checklist'
        verbose_name_plural = 'Checklists'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.area} ({self.estado})"


class Visita(models.Model):
    """
    Modelo para gestionar Visitas de Seguridad
    """
    TIPO_CHOICES = [
        ('preventiva', 'Preventiva'),
        ('correctiva', 'Correctiva'),
        ('seguimiento', 'Seguimiento'),
        ('emergencia', 'Emergencia'),
    ]
    
    RESULTADO_CHOICES = [
        ('satisfactorio', 'Satisfactorio'),
        ('observaciones_menores', 'Observaciones Menores'),
        ('observaciones_mayores', 'Observaciones Mayores'),
        ('critico', 'Crítico'),
    ]
    
    codigo_visita = models.CharField(max_length=50, unique=True, verbose_name="Código de Visita")
    tipo_visita = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES,
        verbose_name="Tipo de Visita"
    )
    fecha_visita = models.DateField(verbose_name="Fecha de Visita")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    hora_fin = models.TimeField(verbose_name="Hora de Fin")
    lugar = models.CharField(max_length=200, verbose_name="Lugar")
    inspector = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='visitas_inspeccion',
        verbose_name="Inspector"
    )
    checklist = models.ForeignKey(
        Checklist, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='visitas',
        verbose_name="Checklist Asociado"
    )
    hallazgos = models.TextField(verbose_name="Hallazgos")
    resultado = models.CharField(
        max_length=30, 
        choices=RESULTADO_CHOICES,
        verbose_name="Resultado"
    )
    recomendaciones = models.TextField(verbose_name="Recomendaciones")
    requiere_seguimiento = models.BooleanField(default=False, verbose_name="Requiere Seguimiento")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    class Meta:
        db_table = 'visitas'
        verbose_name = 'Visita de Seguridad'
        verbose_name_plural = 'Visitas de Seguridad'
        ordering = ['-fecha_visita', '-hora_inicio']
    
    def __str__(self):
        return f"{self.codigo_visita} - {self.lugar} ({self.fecha_visita})"
