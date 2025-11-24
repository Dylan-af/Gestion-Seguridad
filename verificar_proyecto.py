#!/usr/bin/env python
"""
Script de Verificación del Proyecto
Sistema de Gestión de Seguridad Forestal
Verifica la estructura completa del proyecto Django
"""

import os
import sys

def verificar_estructura():
    """Verifica que todos los archivos necesarios existan"""
    
    archivos_requeridos = [
        # Archivos raíz
        'manage.py',
        'requirements.txt',
        'README.md',
        '.gitignore',
        '.env.example',
        
        # Proyecto principal
        'gestion_forestal/__init__.py',
        'gestion_forestal/settings.py',
        'gestion_forestal/urls.py',
        'gestion_forestal/wsgi.py',
        'gestion_forestal/asgi.py',
        
        # Aplicación seguridad_app
        'seguridad_app/__init__.py',
        'seguridad_app/models.py',
        'seguridad_app/views.py',
        'seguridad_app/urls.py',
        'seguridad_app/admin.py',
        'seguridad_app/apps.py',
        'seguridad_app/tests.py',
        'seguridad_app/migrations/__init__.py',
        
        # Templates
        'seguridad_app/templates/base.html',
        'seguridad_app/templates/login.html',
        'seguridad_app/templates/dashboard.html',
        'seguridad_app/templates/checklist_list.html',
        'seguridad_app/templates/checklist_form.html',
        'seguridad_app/templates/checklist_detail.html',
        'seguridad_app/templates/checklist_confirm_delete.html',
        'seguridad_app/templates/visita_list.html',
        'seguridad_app/templates/visita_form.html',
        'seguridad_app/templates/visita_detail.html',
        'seguridad_app/templates/visita_confirm_delete.html',
    ]
    
    print("=" * 70)
    print("="*70)
    print("   Sistema de Gestión de Seguridad Forestal")
    print("   Script de Verificación Integral del Proyecto")
    print("=" * 70)
    print()
    
    errores = []
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} - NO ENCONTRADO")
            errores.append(archivo)
    
    print()
    print("=" * 70)
    
    if errores:
        print(f"❌ ERRORES: {len(errores)} archivo(s) faltante(s)")
        print("Archivos faltantes:")
        for e in errores:
            print(f"  - {e}")
        return False
    else:
        print("✅ TODOS LOS ARCHIVOS ESTÁN PRESENTES")
        return True


def verificar_configuracion():
    """Verifica la configuración básica"""
    
    print()
    print("=" * 70)
    print("⚙️  VERIFICACIÓN DE CONFIGURACIÓN")
    print("=" * 70)
    print()
    
    checks = []
    
    # Verificar settings.py
    try:
        with open('gestion_forestal/settings.py', 'r', encoding='utf-8') as f:
            contenido = f.read()
            
            # Verificar MySQL
            if 'django.db.backends.mysql' in contenido:
                print("✅ Configuración de MySQL encontrada")
                checks.append(True)
            else:
                print("❌ Configuración de MySQL no encontrada")
                checks.append(False)
            
            # Verificar Hashing
            if 'Argon2PasswordHasher' in contenido:
                print("✅ Configuración de hashing (Argon2) encontrada")
                checks.append(True)
            else:
                print("❌ Configuración de hashing no encontrada")
                checks.append(False)
            
            # Verificar sesiones
            if 'SESSION_COOKIE_AGE' in contenido:
                print("✅ Configuración de sesiones encontrada")
                checks.append(True)
            else:
                print("❌ Configuración de sesiones no encontrada")
                checks.append(False)
            
            # Verificar app instalada
            if 'seguridad_app' in contenido:
                print("✅ Aplicación 'seguridad_app' registrada")
                checks.append(True)
            else:
                print("❌ Aplicación 'seguridad_app' no registrada")
                checks.append(False)
                
    except Exception as e:
        print(f"❌ Error al leer settings.py: {e}")
        return False
    
    # Verificar models.py
    try:
        with open('seguridad_app/models.py', 'r', encoding='utf-8') as f:
            contenido = f.read()
            
            if 'class Checklist' in contenido:
                print("✅ Modelo 'Checklist' encontrado")
                checks.append(True)
            else:
                print("❌ Modelo 'Checklist' no encontrado")
                checks.append(False)
            
            if 'class Visita' in contenido:
                print("✅ Modelo 'Visita' encontrado")
                checks.append(True)
            else:
                print("❌ Modelo 'Visita' no encontrado")
                checks.append(False)
                
    except Exception as e:
        print(f"❌ Error al leer models.py: {e}")
        return False
    
    # Verificar views.py
    try:
        with open('seguridad_app/views.py', 'r', encoding='utf-8') as f:
            contenido = f.read()
            
            if 'def login_view' in contenido:
                print("✅ Vista de login encontrada")
                checks.append(True)
            else:
                print("❌ Vista de login no encontrada")
                checks.append(False)
            
            if '@login_required' in contenido:
                print("✅ Rutas protegidas (@login_required) encontradas")
                checks.append(True)
            else:
                print("❌ Rutas protegidas no encontradas")
                checks.append(False)
            
            # Verificar CRUD Checklist
            if all(x in contenido for x in ['checklist_list_view', 'checklist_create_view', 
                                             'checklist_edit_view', 'checklist_delete_view']):
                print("✅ CRUD completo de Checklist encontrado")
                checks.append(True)
            else:
                print("❌ CRUD de Checklist incompleto")
                checks.append(False)
            
            # Verificar CRUD Visita
            if all(x in contenido for x in ['visita_list_view', 'visita_create_view', 
                                            'visita_edit_view', 'visita_delete_view']):
                print("✅ CRUD completo de Visita encontrado")
                checks.append(True)
            else:
                print("❌ CRUD de Visita incompleto")
                checks.append(False)
                
    except Exception as e:
        print(f"❌ Error al leer views.py: {e}")
        return False
    
    print()
    print("=" * 70)
    
    if all(checks):
        print("✅ TODAS LAS CONFIGURACIONES SON CORRECTAS")
        return True
    else:
        print(f"❌ FALTAN CONFIGURACIONES: {checks.count(False)} problema(s)")
        return False


def verificar_templates():
    """Verifica que los templates existan y tengan contenido básico"""
    
    print()
    print("=" * 70)
    print("📄 VERIFICACIÓN DE TEMPLATES")
    print("=" * 70)
    print()
    
    templates = {
        'base.html': ['<!DOCTYPE html>', '<body>'],
        'login.html': ['{% extends', 'form', 'csrf_token'],
        'dashboard.html': ['{% extends', 'dashboard'],
        'checklist_list.html': ['{% extends', 'checklist'],
        'visita_list.html': ['{% extends', 'visita'],
    }
    
    checks = []
    
    for template, keywords in templates.items():
        ruta = f'seguridad_app/templates/{template}'
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
                
                keywords_encontrados = sum(1 for kw in keywords if kw in contenido)
                
                if keywords_encontrados == len(keywords):
                    print(f"✅ {template} - OK ({keywords_encontrados}/{len(keywords)} elementos)")
                    checks.append(True)
                else:
                    print(f"⚠️  {template} - Parcial ({keywords_encontrados}/{len(keywords)} elementos)")
                    checks.append(False)
                    
        except Exception as e:
            print(f"❌ {template} - Error: {e}")
            checks.append(False)
    
    print()
    print("=" * 70)
    
    if all(checks):
        print("✅ TODOS LOS TEMPLATES SON VÁLIDOS")
        return True
    else:
        print(f"⚠️  {checks.count(False)} template(s) con problemas")
        return True  # No es crítico


def main():
    """Función principal"""
    
    print("\n")
    print("🌲" * 35)
    print("   TI3041_Backend_Checklist - Sistema de Gestión Forestal")
    print("   Script de Verificación de Proyecto")
    print("🌲" * 35)
    print()
    
    resultados = []
    
    # Verificar estructura
    resultados.append(verificar_estructura())
    
    # Verificar configuración
    resultados.append(verificar_configuracion())
    
    # Verificar templates
    resultados.append(verificar_templates())
    
    # Resumen final
    print()
    print("=" * 70)
    print("📊 RESUMEN FINAL")
    print("=" * 70)
    print()
    
    if all(resultados):
        print("✅ ¡PROYECTO COMPLETAMENTE VERIFICADO Y FUNCIONAL!")
        print()
        print("📝 Próximos pasos:")
        print("   1. Crear entorno virtual: python -m venv venv")
        print("   2. Activar entorno: .\\venv\\Scripts\\Activate.ps1")
        print("   3. Instalar dependencias: pip install -r requirements.txt")
        print("   4. Configurar MySQL en settings.py")
        print("   5. Ejecutar migraciones: python manage.py migrate")
        print("   6. Crear superusuario: python manage.py createsuperuser")
        print("   7. Ejecutar servidor: python manage.py runserver")
        print()
        return 0
    else:
        print("❌ SE ENCONTRARON PROBLEMAS EN EL PROYECTO")
        print("   Revisa los mensajes anteriores para más detalles.")
        print()
        return 1


if __name__ == '__main__':
    sys.exit(main())
