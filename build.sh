#!/usr/bin/env bash

# Salir en caso de error
set -o errexit

# Modifique esta línea según sea necesario para su administrador de paquetes
pip install -r requirements.txt

# Convertir archivos de activos estático
python manage.py collectstatic --no-input

# Aplicar cualquier migración de base de datos pendiente
python manage.py migrate
