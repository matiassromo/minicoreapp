# MiniCoreApp

MiniCoreApp es una aplicación web desarrollada con Django para la gestión y visualización de gastos filtrados por fechas, con cálculo del total por departamento.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior
- Virtualenv
- PostgreSQL
- Azure CLI (opcional, para despliegue en Azure)
- pip (administrador de paquetes de Python)

## Configuración del proyecto

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone <URL-DEL-REPOSITORIO>
cd MiniCoreApp
```

### 2. Crear y activar un entorno virtual

Crea un entorno virtual y actívalo:

```bash
python -m venv venv
source venv/bin/activate      # Para Linux/Mac
venv\Scripts\activate         # Para Windows
```

### 3. Instalar dependencias

Instala las dependencias necesarias usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crea una base de datos PostgreSQL y configura los detalles de conexión en el archivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Realizar migraciones

Aplica las migraciones para preparar la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Cargar datos iniciales (opcional)

Si deseas cargar datos de ejemplo, puedes usar un archivo fixtures o crear datos manualmente en el panel de administración.

### 7. Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo local:

```bash
python manage.py runserver
```

La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Despliegue en Azure

Sigue estos pasos para desplegar la aplicación en Azure:

### 1. Crear un App Service en Azure

1. Accede al portal de Azure.
2. Crea un nuevo recurso de App Service.
3. Configura el entorno con Python 3.10 o superior.

### 2. Configurar variables de entorno

En el portal de Azure, agrega las siguientes variables de entorno en la sección Configuración:

- `ALLOWED_HOSTS`: tu-dominio.azurewebsites.net
- `DATABASE_URL`: postgresql://usuario:contraseña@host:puerto/base_de_datos

### 3. Desplegar la aplicación

Usa el despliegue continuo desde GitHub o realiza el despliegue manual subiendo los archivos.

## Estructura del proyecto

```bash
MiniCoreApp/
├── core/
│   ├── migrations/
│   ├── templates/core/
│   │   └── filtrar_gastos.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
├── minicoreapp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── staticfiles/
├── manage.py
├── requirements.txt
└── README.md
```

## Funcionalidades

- **Filtrado de gastos**: Filtrar gastos por un rango de fechas seleccionado.
- **Cálculo por departamento**: Muestra el total de gastos por departamento.
- **Panel administrativo**: Gestión de datos mediante el panel de administración de Django.

## Tecnologías utilizadas

- Django 5.1
- Python 3.12
- PostgreSQL
- HTML/CSS (Bootstrap para diseño responsivo)
- Azure App Service (para despliegue)

## Contribuciones

Si deseas contribuir, crea un fork del proyecto y envía un pull request. Para reportar errores o sugerencias, abre un issue.

## Autor

Matías Romo

## Licencia

Este proyecto está bajo la licencia MIT.
