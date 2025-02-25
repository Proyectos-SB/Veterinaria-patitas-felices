from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AplicacionVacunaViewSet

router = DefaultRouter()
router.register(r'aplicaciones', AplicacionVacunaViewSet, basename='aplicacion-vacuna')

urlpatterns = [
    path('', include(router.urls)),
]