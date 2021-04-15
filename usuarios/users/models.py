from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    # PermissionsMixin es para ue nuestro proyecto trabaje con este modelo de usuario y no con el que django
    # trae por defecto; esto tambien se aplica al super usuario que se crea por terminal

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    # AbstractBaseUser nos pide redefinir el is_staff(permiso para que el usuario pueda entrar al admin de django)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()


    # Este campo es para indicar en la creacion de super usuario cual va a ser el nombre de usuario
    # Esto es requerido cuando cambiamos el modelo de usuario que viene por defecto en django para usar nuestro propio modelo
    USERNAME_FIELD = 'username' #'username' parametro que pusimos arriba

    #Los campos que queramos que nos pida como requerido para la creacion de super usuario a demas de los que ya pide que son
    #username y password
    REQUIRED_FIELDS = ['email', ]


    def get_short_name(self):
        return self.username

    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos