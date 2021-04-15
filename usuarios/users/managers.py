from django.db import models 
from django.contrib.auth.models import BaseUserManager #Para podre sobre escribir ciertas funciones necesarias para el
                                                       #super ususario


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        #modelo del models.py; los campos que son requeridos
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        # Esto es para que el password que se esta enviando se encripte
        user.set_password(password)
        # Y ahora guardarlo en la base de datos; como se esta usando solo 1 pues la ponemos asi, pero en caso de que se este
        #trabajando con mas de una se debe especificar en que db se va a guardar poniendolo entre los ()
        user.save(using=self.db)

    
    
    # Necesitamos sobreescribir esta funcion
    def create_user(self, username, email, password=None, **extra_fields):
        self._create_user(username, email, password, False, False, **extra_fields)

    
    # Necesitamos sobreescribir esta funcion
    def create_superuser(self, username, email, password=None, **extra_fields):
        #_create_user -> funcion privada que creamos arriba
        return self._create_user(username, email, password, True, True, **extra_fields)