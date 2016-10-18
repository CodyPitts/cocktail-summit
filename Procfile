web: gunicorn cocktail_summit.wsgi:application --log-file -
worker: celery worker --app=cocktail_summit.tasks