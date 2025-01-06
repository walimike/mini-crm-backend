web: gunicorn mini-crm-backend.wsgi:application --bind 0.0.0.0:$PORT

web: gunicorn mini-crm-backend.wsgi 
web: python manage.py migrate && gunicorn <project_name>.wsg