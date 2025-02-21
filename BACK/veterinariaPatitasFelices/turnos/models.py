from django.db import models
from usuarios.models import Veterinario
from mascotas.models import Mascota
from datetime import timedelta, datetime
import pytz
from django.core.exceptions import ValidationError
from datetime import timedelta
# Create your models here.

class DisponibilidadVeterinario(models.Model):
    veterinario = models.ForeignKey('usuarios.Veterinario', on_delete=models.CASCADE, related_name="disponibilidades")
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        unique_together = ('veterinario', 'fecha', 'hora_inicio')

    def __str__(self):
        return f"{self.veterinario} - {self.fecha} {self.hora_inicio}-{self.hora_fin}"

    @staticmethod
    def generar_disponibilidad(veterinario, dias=30, horario_inicio="08:00", horario_fin="18:00"):
        """
        Genera disponibilidad de lunes a viernes en intervalos de 30 minutos para los próximos 'dias'.
        """
        zona_horaria = pytz.timezone('America/Argentina/Buenos_Aires')
        hoy = datetime.now(zona_horaria).date()
        fecha_inicio = hoy + timedelta(days=1)  # Desde mañana

        for i in range(dias):
            fecha = fecha_inicio + timedelta(days=i)
            if fecha.weekday() < 5:  # 0=Lunes, 4=Viernes 
                hora_actual = datetime.strptime(horario_inicio, "%H:%M").time()
                hora_fin_dt = datetime.strptime(horario_fin, "%H:%M").time()

                while hora_actual < hora_fin_dt:
                    siguiente_hora = (datetime.combine(datetime.today(), hora_actual) + timedelta(minutes=30)).time()

                    if siguiente_hora <= hora_fin_dt:
                        DisponibilidadVeterinario.objects.get_or_create(
                            veterinario=veterinario,
                            fecha=fecha,
                            hora_inicio=hora_actual,
                            hora_fin=siguiente_hora
                        )
                    hora_actual = siguiente_hora




class Turno(models.Model):
    cliente = models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE, related_name='turnos')
    mascota = models.ForeignKey('mascotas.Mascota', on_delete=models.CASCADE, related_name='turnos')
    veterinario = models.ForeignKey('usuarios.Veterinario', on_delete=models.CASCADE, related_name='turnos')
    servicio = models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora = models.TimeField()
    confirmado = models.BooleanField(default=False)

    def clean(self):
        # Verificar disponibilidad horaria del médico
        disponibilidad = DisponibilidadVeterinario.objects.filter(
            veterinario=self.veterinario,
            fecha=self.fecha,
            hora_inicio__lte=self.hora,
            hora_fin__gt=self.hora
        ).exists()

        if not disponibilidad:
            raise ValidationError('El médico no tiene disponibilidad en este horario.')

        # Verificar solapamiento con otros turnos
        solapamiento = Turno.objects.filter(
            veterinario=self.veterinario,
            fecha=self.fecha,
            hora=self.hora
        ).exclude(id=self.id).exists()

        if solapamiento:
            raise ValidationError('El médico ya tiene un turno en ese horario.')

    def save(self, *args, **kwargs):
        self.clean()  # Llama a `clean()` antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Turno de {self.mascota} ({self.cliente}) con {self.veterinario} - {self.servicio.nombre} el {self.fecha} a las {self.hora}"
