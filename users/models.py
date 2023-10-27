from typing import Any
from django.db import models
from django.utils import timezone #"""funciones de fecha""""
from django.contrib.auth.models import ( #"""contiene las definiciones de modelos relacionados con la autenticación y la gestión de usuario"""
    AbstractBaseUser, #se utiliza para personalizar la implementación del modelo de usuario.
    PermissionsMixin, #. Proporciona campos y métodos relacionados con permisos y control de acceso
    UserManager #Es una clase que proporciona métodos útiles para trabajar con modelos de usuario, como la creación de nuevos usuarios.
)
# Create your models here.


class CustomUserManeger (UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Debes tener un correo electronico")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email= None, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email= None, password = None, **extra_fields):
        extra_fields.setdefault("isstaff", True)
        return self._create_user(email, password, **extra_fields)
    
