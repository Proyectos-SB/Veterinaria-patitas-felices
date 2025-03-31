from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from .models import AplicacionVacuna
from .serializers import AplicacionVacunaSerializer 

class AplicacionVacunaViewSet(viewsets.ModelViewSet):
    serializer_class = AplicacionVacunaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar las aplicaciones de vacuna de las mascotas del cliente autenticado
        # Suponiendo que el usuario tiene relación con Cliente y Cliente con Mascota
        return AplicacionVacuna.objects.filter(mascota__cliente=self.request.user)

    def perform_create(self, serializer):
        # Asignamos la mascota de la aplicación de vacuna al cliente autenticado
        # Se espera que el cliente ya tenga asignadas sus mascotas. 
        # Aquí podrías requerir que el request incluya el id de la mascota en los datos.
        mascota_id = self.request.data.get('mascota')
        if not mascota_id:
            raise serializers.ValidationError("El ID de la mascota es requerido.")
        # Aseguramos que la mascota pertenezca al cliente autenticado
        try:
            mascota = self.request.user.mascota_set.get(id=mascota_id)
        except Exception:
            raise serializers.ValidationError("Mascota no encontrada o no pertenece a este cliente.")
        serializer.save(mascota=mascota)
