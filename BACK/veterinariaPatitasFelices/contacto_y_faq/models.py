from django.db import models

# Create your models here.


class Contacto(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    telefono = models.CharField(max_length=20) 
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
        

class FAQ(models.Model):

    pregunta = models.CharField(max_length=100)
    descripcion = models.TextField()
