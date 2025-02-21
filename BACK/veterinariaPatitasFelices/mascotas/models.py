from django.db import models

# Create your models here.
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
    peso = models.IntegerField(max_length=3)

    def __str__(self):
        return self.nombre