from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarritoCompraViewSet, ItemCarritoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'carrito', CarritoCompraViewSet, basename='carrito')
router.register(r'items', ItemCarritoViewSet, basename='item-carrito')
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', include(router.urls)),
]