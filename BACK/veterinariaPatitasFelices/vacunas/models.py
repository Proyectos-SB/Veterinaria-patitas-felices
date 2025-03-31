from django.db import models
from mascotas.models import Mascota  # Importamos el modelo Mascota de la app mascotas

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class AplicacionVacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='vacunaciones')
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE, related_name='aplicaciones')
    fecha_aplicacion = models.DateField()
    proximo_refuerzo = models.DateField(null=True, blank=True)  # Opcional, para el próximo refuerzo

    def __str__(self):
        return f"{self.vacuna.nombre} en {self.mascota.nombre} - {self.fecha_aplicacion}"