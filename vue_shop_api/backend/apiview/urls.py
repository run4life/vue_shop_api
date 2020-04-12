from django.conf.urls import url

from backend.apiview.login.views import LoginView
from backend.apiview.user.views import (UserView, UsersView, UserStateView, UserRoleView)
from backend.apiview.right.views import (RightsView, MenusView)
from backend.apiview.role.views import (RolesView, RoleView, RoleRightView)

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^users$', UsersView.as_view()),
    url(r'^users/(?P<user_id>\d+)$', UserView.as_view()),
    url(r'^users/(?P<user_id>\d+)/role$', UserRoleView.as_view()),
    url(r'^users/(?P<user_id>\d+)/state/(?P<type>.+)$', UserStateView.as_view()),
    url(r'^rights/(?P<type>.+)$', RightsView.as_view()),
    url(r'^roles$', RolesView.as_view()),
    url(r'^roles/(?P<role_id>\d+)$', RoleView.as_view()),
    url(r'^roles/(?P<role_id>\d+)/rights$', RoleRightView.as_view()),
    url(r'^menus$', MenusView.as_view()),
    ]