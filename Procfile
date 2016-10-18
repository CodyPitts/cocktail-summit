web: gunicorn cocktail_summit.wsgi:application --log-file -
worker: celery worker --app=tasks.app