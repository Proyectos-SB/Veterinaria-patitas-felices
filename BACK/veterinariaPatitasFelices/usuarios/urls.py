from django.urls import path
from .views import ClienteRegistroAPIView, LoginAPIView,ObtenerUsuarioAutenticadoAPIView, ActualizarUsuarioAPIView

urlpatterns = [
    path('registro/', ClienteRegistroAPIView.as_view(), name='registro'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('me/', ObtenerUsuarioAutenticadoAPIView.as_view(), name='obtener_usuario_autenticado'),
    path('me/editar/', ActualizarUsuarioAPIView.as_view(), name='actualizar_usuario'),
]