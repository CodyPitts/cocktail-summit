web: gunicorn cocktail_summit.wsgi:application --log-file -
worker: python manage.py celery worker --loglevel=info