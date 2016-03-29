web: python manage.py makemigrations
web: python manage.py migrate
web: python manage.py createsuperuser
web: sudo python manage.py collectstatic --noinput
web: rm -rf static/
web: gunicorn gunicorn_test.wsgi:application
