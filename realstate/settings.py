"""
Django settings for realstate project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import os
# *CONFIGURACION PARA DEPLOY EN RENDER*
import dj_database_url

from django.contrib.messages import constants as mensajes_de_error # para trabajar con msj de error 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# *CONFIGURACION PARA DEPLOY EN RENDER*
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
# *CONFIGURACION PARA DEPLOY EN RENDER*
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

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
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
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

STATIC_URL = '/static/'

# *CONFIGURACION PARA DEPLOY EN RENDER*
if not DEBUG:
# Indica a Django que copie los activos estáticos en una ruta llamada staticfiles` (esto es específico de Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Habilite el backend de almacenamiento WhiteNoise, que comprime archivos estáticos para reducir el uso del disco
# y cambia el nombre de los archivos con nombres únicos para cada versión para admitir el almacenamiento en caché a largo plazo
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# configuracion de email:

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # Configuración del backend de email de Django
EMAIL_HOST = "smtp-mail.outlook.com"  # Host SMTP de Hotmail (Outlook)
EMAIL_USE_TLS = True  # Utilizar TLS
EMAIL_PORT = 587  # Puerto SMTP para TLS
EMAIL_HOST_USER='leo_91_166@hotmail.com' #direccion de correo electronico
EMAIL_HOST_PASSWORD='paozgadndgittrdq' #agregamos la contraseña de nuestro correo 

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