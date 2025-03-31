from rest_framework import viewsets, permissions
from .models import Mascota
from .serializers import MascotaSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retorna solo las mascotas asociadas al cliente autenticado
        return Mascota.objects.filter(cliente=self.request.user.cliente)

    def perform_create(self, serializer):
        # Asigna automáticamente el cliente autenticado a la mascota que se crea
        serializer.save(cliente=self.request.user.cliente)