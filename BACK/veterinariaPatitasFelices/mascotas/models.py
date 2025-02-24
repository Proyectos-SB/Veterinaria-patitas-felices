from django.db import models

# Create your models here.
class TipoMascota(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    SEXO_MASCOTA = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
        ('-', '-'),
    ]
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20, choices=SEXO_MASCOTA, default='-')
    tipo = models.ForeignKey(TipoMascota, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nombre
