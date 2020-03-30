# django-api-server

pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install djangorestframework -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django-rest-swagger -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install djangorestframework-jwt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install djangorestframework_simplejwt -i https://pypi.tuna.tsinghua.edu.cn/simple

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