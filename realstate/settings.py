"""
Django settings for realstate project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from google.oauth2 import service_account

import os
# *CONFIGURACION PARA DEPLOY EN RENDER*
import dj_database_url

from django.contrib.messages import constants as mensajes_de_error # para trabajar con msj de error 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# *CONFIGURACION PARA DEPLOY EN RENDER*
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key') # Aquí se usa la variable de entorno

# SECURITY WARNING: don't run with debug turned on in production!
# *CONFIGURACION PARA DEPLOY EN RENDER*
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['realestate-crud-qxko.onrender.com', 'localhost']

# *CONFIGURACION PARA DEPLOY EN RENDER*
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'realestateapp',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # *CONFIGURACION PARA DEPLOY EN RENDER*
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'realstate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'realstate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# *CONFIGURACION PARA DEPLOY EN RENDER*
# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        #default=os.environ.get('DATABASE_URL'),  # Aquí se usa la variable de entorno
        default='postgresql://realestatadb_user:EHyBJ4I2TsZlT89UHbpZjjnvqpJne0zI@dpg-crllckbv2p9s73e0q0ig-a.oregon-postgres.render.com/realestatadb',
        conn_max_age=600,
        ssl_require=True  # Mantén esta línea si tu base de datos requiere SSL
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Configuración de archivos estáticos
STATIC_URL = '/static/'  # Añade esta línea
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'realestateapp/static'),
]

# Configuración para archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Mueve esta línea fuera del bloque if not DEBUG
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Mantén esta línea aquí

# Configuración para entorno de producción
if not DEBUG:
    # Aquí podrías tener otra configuración relacionada con producción
    pass  # Este bloque puede quedar vacío o puedes agregar configuraciones específicas para producción

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# configuracion de email:

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # Backend de email
EMAIL_HOST = "smtp-mail.outlook.com"  # Host SMTP de Hotmail (Outlook)
EMAIL_USE_TLS = True  # Usar TLS
EMAIL_PORT = 587  # Puerto SMTP para TLS
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # Dirección de correo electrónico desde variable de entorno
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # Contraseña de correo electrónico desde variable de entorno

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" #importamos crispy para trabajar con formularios 
CRISPY_TEMPLATE_PACK = "bootstrap5"

#cargamos los tipos de msj de error

MESSAGE_TAGS={
    mensajes_de_error.DEBUG:'deburg',
    mensajes_de_error.INFO:'info',
    mensajes_de_error.SUCCESS:'success',
    mensajes_de_error.WARNING:'warning',
    mensajes_de_error.ERROR:'danger',
}

LOGIN_URL = '/authentication/logear/'  # Define la URL a la que se redirige si no estás autenticado
LOGIN_REDIRECT_URL = 'home'  # Redirige a 'home' después de iniciar sesión

APPEND_SLASH = True

# Configuración de Google Cloud Storage
from google.oauth2 import service_account

# Cargar las credenciales desde el archivo JSON
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
)

DEFAULT_FILE_STORAGE = 'DJANGO-PROYECT001.gcloud.GoogleCloudMediaFileStorage'

GS_BUCKET_NAME = os.environ.get('GS_BUCKET_NAME')  # Usa la variable de entorno para el nombre del bucket
GS_BUCKET_ID = os.environ.get('GS_PROJECT_ID') # Usa la variable de entorno para el ID del bucket

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)
MEDIA_ROOT= "media/"
UPLOAD_ROOT = 'media/uploads/'

#DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'