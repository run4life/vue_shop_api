from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from matplotlib.backends import backend



API_VERSIONS = [url(r'^v1/', include('backend.apiview.urls'))]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/private/', include(API_VERSIONS))
]
