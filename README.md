# Sistema de Gestión de Seguridad Forestal

Sistema web para la gestión de checklists de seguridad y visitas de inspección en operaciones forestales.

## Características

- Sistema de autenticación de usuarios
- CRUD completo para Checklists
- CRUD completo para Visitas de inspección
- Relaciones entre entidades con ForeignKey
- Dashboard con estadísticas
- Contraseñas hasheadas con PBKDF2
- Sesiones seguras con tiempo de expiración
- Protección CSRF en formularios

## Tecnologías

- Django 4.2.7
- MySQL 8.0
- Python 3.8+
- PyMySQL 1.1.0
- HTML/CSS

## Instalación

Ver [INSTALL.md](INSTALL.md) para instrucciones detalladas.

### Inicio rápido

```bash
# Clonar repositorio
git clone https://github.com/Dylan-af/Gestion-Seguridad.git
cd Gestion-Seguridad

# Crear entorno virtual e instalar dependencias
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Configurar base de datos MySQL
CREATE DATABASE `gestion-forestal`;

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

Acceder en: http://127.0.0.1:8000/login/

## Estructura del Proyecto

```
gestion_forestal/          # Configuración principal Django
├── settings.py            # Configuración del proyecto
├── urls.py                # URLs principales
└── wsgi.py                # Configuración WSGI

seguridad_app/             # Aplicación principal
├── models.py              # Modelos Checklist y Visita
├── views.py               # Lógica de vistas
├── urls.py                # URLs de la aplicación
├── forms.py               # Formularios Django
├── templates/             # Templates HTML
└── migrations/            # Migraciones de base de datos
```

## Modelos de Datos

### Checklist

- titulo (CharField)
- descripcion (TextField)
- estado (CharField): pendiente, en_progreso, completado, cancelado
- prioridad (CharField): baja, media, alta, critica
- fecha_creacion (DateTimeField)
- fecha_actualizacion (DateTimeField)
- usuario (ForeignKey → User)

### Visita

- lugar (CharField)
- tipo (CharField): preventiva, correctiva, seguimiento, emergencia
- fecha_visita (DateField)
- resultado (CharField): satisfactorio, observaciones_menores, observaciones_mayores, critico
- observaciones (TextField)
- fecha_creacion (DateTimeField)
- checklist (ForeignKey → Checklist)
- inspector (ForeignKey → User)

## Rutas Principales

```
/login/                     # Inicio de sesión
/logout/                    # Cierre de sesión
/dashboard/                 # Panel principal

/checklists/                # Listado de checklists
/checklists/crear/          # Crear checklist
/checklists/editar/<id>/    # Editar checklist
/checklists/eliminar/<id>/  # Eliminar checklist
/checklists/detalle/<id>/   # Ver detalle

/visitas/                   # Listado de visitas
/visitas/crear/             # Crear visita
/visitas/editar/<id>/       # Editar visita
/visitas/eliminar/<id>/     # Eliminar visita
/visitas/detalle/<id>/      # Ver detalle
```

## Configuración de Base de Datos

Editar `gestion_forestal/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion-forestal',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Seguridad

- Contraseñas hasheadas con PBKDF2
- Protección CSRF habilitada
- Sesiones HTTP-only
- Rutas protegidas con @login_required
- Validación de formularios server-side

## Desarrollo

### Comandos útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Iniciar shell de Django
python manage.py shell

# Colectar archivos estáticos
python manage.py collectstatic
```

### Estructura de templates

Los templates utilizan herencia con `base.html` como plantilla principal.

```
templates/
├── base.html                   # Template base
├── login.html                  # Página de login
├── dashboard.html              # Dashboard principal
├── checklist_list.html         # Listado de checklists
├── checklist_create.html       # Crear checklist
├── checklist_edit.html         # Editar checklist
├── checklist_delete.html       # Confirmar eliminación
├── checklist_detail.html       # Detalle de checklist
├── visita_list.html            # Listado de visitas
├── visita_create.html          # Crear visita
├── visita_edit.html            # Editar visita
├── visita_delete.html          # Confirmar eliminación
└── visita_detail.html          # Detalle de visita
```

## Licencia

MIT License

## Autor

Dylan Merino
- GitHub: [@Dylan-af](https://github.com/Dylan-af)
- Email: dylan.merino@inacapmail.cl
