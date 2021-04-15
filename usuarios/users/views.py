from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserRegisterForm


# Create your views here.


# Siempre para crear un usuario lo mejor es utilizar el FormView
class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/'

    # Para que un FormView haga un porceso siempre necesita la funcion:
    def form_valid(self,form):

        # el create_user es del managers.py; la funcion recibe (username, email, password=None, **extra_fields) asi
        # que se los damos en el orden que los debe recibir y los que son campos extras le ponemos variable y de
        # que campo del form sale ese dato
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero']
        )
        
        return super(UserRegisterView, self).form_valid(form)


class LoginView(views.LoginView):
    template_name = 'users/login.html'
    #Tenemos que poner (LOGIN_REDIRECT_URL = '/') en setting.py para cambiar la direccion
    #que tiene por defecto el LoginView cuando se le da entrar para entrar; entre '' ponemos
    #La direccion a la que queremos que vaya, en este caso al home u inicio.



class LogoutView(LoginRequiredMixin ,views.LogoutView):
    template_name = 'users/log_out.html'