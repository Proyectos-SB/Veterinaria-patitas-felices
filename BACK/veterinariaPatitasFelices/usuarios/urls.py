from django.urls import path
from .views import ClienteRegistroAPIView, LoginAPIView

urlpatterns = [
    path('registro/', ClienteRegistroAPIView.as_view(), name='registro'),
    path('login/', LoginAPIView.as_view(), name='login'),
]