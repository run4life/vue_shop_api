from django.conf.urls import url

from backend.apiview.login.views import LoginView
from backend.apiview.user.views import (UserView, UsersView)

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^users$', UsersView.as_view()),
    url(r'^users/(?P<user_id>\d+)$', UserView.as_view()),
    ]