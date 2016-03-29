web: sudo nginx
web: python manage.py makemigrations
web: python manage.py migrate
web: python manage.py createsuperuser
web: echo "from django.contrib.auth.models import User; User.objects.create_superuser('myadmin', 'myemail@example.com', 'hunter2')" | python manage.py shell
web: python manage.py collectstatic --noinput
web: sudo nginx -s reload
web: gunicorn gunicorn_test.wsgi:application
