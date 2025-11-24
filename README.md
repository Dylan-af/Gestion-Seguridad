# 🌲 TI3041_Backend_Checklist - Sistema de Gestión Forestal

## 📋 Descripción del Proyecto

Sistema web desarrollado en **Django (Python)** para la **Gestión de Visitas de Seguridad y Checklists Operacionales** en una empresa forestal.

Este proyecto corresponde a la **Evaluación N°3** de la asignatura **TI3041 - Programación Backend**.

---

## 🎯 Funcionalidades Principales

### ✅ CRUD de Entidades

1. **Checklists Operacionales**
   - Crear, leer, actualizar y eliminar checklists
   - Gestión de estados: Pendiente, En Progreso, Completado, Cancelado
   - Niveles de prioridad: Baja, Media, Alta, Crítica
   - Asignación de responsables y áreas forestales

2. **Visitas de Seguridad**
   - Crear, leer, actualizar y eliminar visitas
   - Tipos de visita: Preventiva, Correctiva, Seguimiento, Emergencia
   - Registro de hallazgos, recomendaciones y resultados
   - Vinculación con checklists operacionales

### 🔐 Seguridad y Sesiones

- **Sistema de autenticación** con login/logout
- **Rutas protegidas** mediante decoradores `@login_required`
- **Hashing de contraseñas** utilizando:
  - Argon2PasswordHasher (principal)
  - PBKDF2PasswordHasher
  - BCryptSHA256PasswordHasher
- **Gestión de sesiones** con tiempo de expiración configurable
- **Protección CSRF** en formularios

### 📊 Dashboard

- Vista general con estadísticas de checklists y visitas
- Listados de registros recientes
- Indicadores visuales de estados y prioridades

---

## 🗂️ Estructura del Proyecto

```
job1/
├── gestion_forestal/           # Proyecto principal Django
│   ├── __init__.py
│   ├── settings.py            # Configuración (MySQL, Hashing, Sesiones)
│   ├── urls.py                # URLs principales del proyecto
│   ├── wsgi.py                # Configuración WSGI
│   └── asgi.py                # Configuración ASGI
│
├── seguridad_app/              # Aplicación principal
│   ├── migrations/             # Migraciones de base de datos
│   │   └── __init__.py
│   ├── templates/              # Plantillas HTML
│   │   ├── base.html          # Template base
│   │   ├── login.html         # Página de inicio de sesión
│   │   ├── dashboard.html     # Dashboard principal
│   │   ├── checklist_list.html
│   │   ├── checklist_form.html
│   │   ├── checklist_detail.html
│   │   ├── checklist_confirm_delete.html
│   │   ├── visita_list.html
│   │   ├── visita_form.html
│   │   ├── visita_detail.html
│   │   └── visita_confirm_delete.html
│   ├── static/                 # Archivos estáticos (CSS, JS, imágenes)
│   ├── __init__.py
│   ├── admin.py               # Configuración del admin de Django
│   ├── apps.py                # Configuración de la aplicación
│   ├── models.py              # Modelos: Checklist y Visita
│   ├── views.py               # Vistas y controladores
│   ├── urls.py                # URLs de la aplicación
│   └── tests.py               # Tests unitarios
│
├── manage.py                   # Utilidad de gestión de Django
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

- **Framework Backend:** Django 4.2.7
- **Lenguaje:** Python 3.10+
- **Base de Datos:** MySQL 8.0
- **ORM:** Django ORM
- **Frontend:** HTML5, CSS3 (templates Django)
- **Seguridad:** Argon2, PBKDF2, BCrypt
- **Conector BD:** mysqlclient

---

## 📦 Instalación y Configuración

### 1. Requisitos Previos

- Python 3.10 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)

### 2. Clonar o descargar el proyecto

```bash
cd c:\Users\Dylan\Documents\job1
```

### 3. Crear entorno virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 5. Configurar Base de Datos MySQL

Crear la base de datos en MySQL:

```sql
CREATE DATABASE gestion_forestal_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'gestion_user'@'localhost' IDENTIFIED BY 'tu_password_seguro';
GRANT ALL PRIVILEGES ON gestion_forestal_db.* TO 'gestion_user'@'localhost';
FLUSH PRIVILEGES;
```

Editar `gestion_forestal/settings.py` con las credenciales:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_forestal_db',
        'USER': 'gestion_user',
        'PASSWORD': 'tu_password_seguro',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. Realizar migraciones

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear superusuario

```powershell
python manage.py createsuperuser
```

Seguir las instrucciones para crear el usuario administrador.

### 8. Ejecutar el servidor de desarrollo

```powershell
python manage.py runserver
```

Acceder a: **http://127.0.0.1:8000/**

---

## 🔑 Acceso al Sistema

### Usuario por Defecto

Después de crear el superusuario, puedes acceder con esas credenciales:

- **URL de Login:** http://127.0.0.1:8000/login/
- **URL de Admin:** http://127.0.0.1:8000/admin/

---

## 📱 Rutas Principales

| Ruta | Descripción | Protegida |
|------|-------------|-----------|
| `/` | Redirige al login | No |
| `/login/` | Página de inicio de sesión | No |
| `/logout/` | Cerrar sesión | Sí |
| `/dashboard/` | Dashboard principal | Sí |
| `/checklists/` | Listado de checklists | Sí |
| `/checklists/crear/` | Crear checklist | Sí |
| `/checklists/<id>/` | Detalle de checklist | Sí |
| `/checklists/<id>/editar/` | Editar checklist | Sí |
| `/checklists/<id>/eliminar/` | Eliminar checklist | Sí |
| `/visitas/` | Listado de visitas | Sí |
| `/visitas/crear/` | Crear visita | Sí |
| `/visitas/<id>/` | Detalle de visita | Sí |
| `/visitas/<id>/editar/` | Editar visita | Sí |
| `/visitas/<id>/eliminar/` | Eliminar visita | Sí |

---

## 🗃️ Modelos de Datos

### Modelo Checklist

```python
- titulo: CharField (título del checklist)
- descripcion: TextField (descripción detallada)
- area: CharField (área forestal)
- responsable: ForeignKey (usuario responsable)
- estado: CharField (pendiente, en_progreso, completado, cancelado)
- prioridad: CharField (baja, media, alta, critica)
- fecha_creacion: DateTimeField
- fecha_vencimiento: DateField
- observaciones: TextField (opcional)
```

### Modelo Visita

```python
- codigo_visita: CharField (código único)
- tipo_visita: CharField (preventiva, correctiva, seguimiento, emergencia)
- fecha_visita: DateField
- hora_inicio: TimeField
- hora_fin: TimeField
- lugar: CharField
- inspector: ForeignKey (usuario inspector)
- checklist: ForeignKey (checklist asociado, opcional)
- hallazgos: TextField
- resultado: CharField (satisfactorio, observaciones_menores, observaciones_mayores, critico)
- recomendaciones: TextField
- requiere_seguimiento: BooleanField
- fecha_creacion: DateTimeField
- fecha_actualizacion: DateTimeField
```

---

## 🔒 Características de Seguridad Implementadas

1. **Autenticación de usuarios** mediante Django Authentication
2. **Hashing robusto de contraseñas** con múltiples algoritmos
3. **Sesiones seguras** con configuración de cookies HTTPOnly
4. **Protección CSRF** en todos los formularios
5. **Rutas protegidas** con decorador `@login_required`
6. **Validación de contraseñas** con requisitos mínimos
7. **Redirección automática** para usuarios no autenticados

---

## 🧪 Pruebas

### Ejecutar tests unitarios

```powershell
python manage.py test seguridad_app
```

---

## 📚 Documentación Adicional

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

## 👥 Autor

**Proyecto Académico - TI3041**  
Instituto/Universidad: [Tu Institución]  
Fecha: Noviembre 2025

---

## 📄 Licencia

Este proyecto es de uso educativo y académico para la Evaluación N°3 de TI3041.

---

## 🐛 Resolución de Problemas

### Error al instalar mysqlclient en Windows

Si encuentras problemas al instalar `mysqlclient`, puedes:

1. Instalar Visual C++ Build Tools
2. O usar PyMySQL como alternativa:

```powershell
pip install pymysql
```

Y agregar en `gestion_forestal/__init__.py`:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

### Error de migraciones

Si tienes problemas con las migraciones:

```powershell
python manage.py migrate --run-syncdb
```

---

## 📞 Soporte

Para preguntas o problemas relacionados con el proyecto, contactar a través de los canales oficiales de la asignatura TI3041.
