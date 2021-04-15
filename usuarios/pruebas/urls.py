from django.urls import path
from . import views

app_name = 'pruebas'

urlpatterns = [
    path(
        route = 'home/',
        view = views.HomeView.as_view(),
        name = 'home'
    ),
]