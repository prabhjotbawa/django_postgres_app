#!/bin/sh
set -e
# run migration
python manage.py migrate --noinput
# Collect static files
python manage.py collectstatic --noinput

python -m gunicorn myproject.wsgi:application -b 0.0.0.0:5001 --timeout 0
