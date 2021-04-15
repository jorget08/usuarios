from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        route = 'register/',
        view = views.UserRegisterView.as_view(),
        name = 'register'
    ),
    path(
        route = 'login/',
        view = views.LoginView.as_view(),
        name = 'login'
    ),
    path(
        route = 'logout/',
        view = views.LogoutView.as_view(),
        name = 'logout'
    ),
]