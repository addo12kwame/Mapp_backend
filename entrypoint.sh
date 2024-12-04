#!/bin/bash
set -e



# Run Django commands
python manage.py makemigrations
python manage.py migrate
python cs_standards_imports.py

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000
