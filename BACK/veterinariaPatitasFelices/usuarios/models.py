from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Cliente(Usuario):
    user = models.OneToOneField('usuarios.CustomUser', on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medico(Usuario):
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"
