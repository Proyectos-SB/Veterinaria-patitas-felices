from django.db import models
from mascotas.models import Mascota
# Create your models here.
class HistoriaClinica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Historia Clinica de {self.mascota.nombre}"
   