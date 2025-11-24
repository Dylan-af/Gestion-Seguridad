# Instalación

## Requisitos

- Python 3.8+
- MySQL Server
- pip

## Instalación Rápida

### 1. Clonar repositorio

```bash
git clone https://github.com/Dylan-af/Gestion-Seguridad.git
cd Gestion-Seguridad
```

### 2. Configurar entorno

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

### 3. Configurar base de datos

Crear base de datos MySQL:

```sql
CREATE DATABASE `gestion-forestal` CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

Editar `gestion_forestal/settings.py` con tus credenciales MySQL:

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

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear usuario administrador

```bash
python manage.py createsuperuser
```

### 6. Iniciar servidor

```bash
python manage.py runserver
```

Acceder en: http://127.0.0.1:8000/login/

## Configuración Avanzada

### Variables de entorno (opcional)

Crear archivo `.env`:

```
DEBUG=True
SECRET_KEY=tu-clave-secreta
DB_NAME=gestion-forestal
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### Servidor de producción

Para producción, configurar:

- `DEBUG = False` en settings.py
- Configurar `ALLOWED_HOSTS`
- Usar servidor WSGI (Gunicorn, uWSGI)
- Configurar servidor web (Nginx, Apache)

## Solución de problemas

### Error de conexión MySQL

Verificar que MySQL esté corriendo y las credenciales sean correctas.

### Error "Port already in use"

```bash
python manage.py runserver 8080
```

### Problemas con pymysql

```bash
pip install pymysql
```
