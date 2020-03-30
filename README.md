# django-api-server

python manage.py startapp posts
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

python manage.py shell
from django.contrib.auth.models import User 
user = User.objects.get(username='admin') 
user.set_password('admin') 
user.save()