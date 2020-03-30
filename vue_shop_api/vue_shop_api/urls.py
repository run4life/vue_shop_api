from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from backend.views import CodeViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(prefix='code', viewset=CodeViewSet, base_name='code')

API_V1 = []

API_V1.extend(router.urls)

API_VERSIONS = [url(r'^v1/', include(API_V1))]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(API_VERSIONS)),
    url(r'^login/', obtain_jwt_token),
]
