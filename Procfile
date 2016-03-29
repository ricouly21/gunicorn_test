web: python manage.py makemigrations
web: python manage.py migrate
web: python manage.py createsuperuser
web: python manage.py collectstatic --noinput
web: gunicorn gunicorn_test.wsgi:application
