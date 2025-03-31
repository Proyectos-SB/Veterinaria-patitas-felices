from .models import Cliente
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import CarritoCompra, ItemCarrito, Pedido, ItemPedido
from .serializers import CarritoCompraSerializer, ItemCarritoSerializer, PedidoSerializer
from django.shortcuts import get_object_or_404

class CarritoCompraViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Retorna el carrito del cliente autenticado
        carrito, created = CarritoCompra.objects.get_or_create(cliente=request.user.cliente)
        serializer = CarritoCompraSerializer(carrito)
        return Response(serializer.data)

class ItemCarritoViewSet(viewsets.ModelViewSet):
    serializer_class = ItemCarritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        carrito, _ = CarritoCompra.objects.get_or_create(cliente=self.request.user.cliente)
        return ItemCarrito.objects.filter(carrito=carrito)

    def perform_create(self, serializer):
        carrito, _ = CarritoCompra.objects.get_or_create(cliente=self.request.user.cliente)
        serializer.save(carrito=carrito)

# Endpoint para convertir el carrito en pedido


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(cliente=self.request.user.cliente)

    @action(detail=False, methods=['post'])
    def crear_pedido(self, request):
        # Obtener el carrito del cliente
        carrito, _ = CarritoCompra.objects.get_or_create(cliente=request.user.cliente)
        items = carrito.items.all()
        if not items.exists():
            return Response({"error": "El carrito está vacío."}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el pedido
        # Se asume que el método de pago se envía en la request
        metodo_pago = request.data.get('metodo_pago')
        if not metodo_pago:
            return Response({"error": "El método de pago es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        pedido = Pedido.objects.create(cliente=request.user.cliente, metodo_pago=metodo_pago)
        # Crear los items del pedido
        for item in items:
            ItemPedido.objects.create(
                pedido=pedido,
                articulo=item.articulo,
                cantidad=item.cantidad,
                precio_unitario=item.articulo.precio
            )
            # Opcional: reducir stock del artículo
            item.articulo.stock -= item.cantidad
            item.articulo.save()
        pedido.save()  # Actualiza total automáticamente en el método save() del modelo
        # Vaciar el carrito
        carrito.items.all().delete()
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Endpoint para "pagar" el pedido (simulación)
    @action(detail=True, methods=['post'])
    def pagar(self, request, pk=None):
        pedido = get_object_or_404(Pedido, pk=pk, cliente=request.user.cliente)
        if pedido.estado != 'Pendiente':
            return Response({"error": "El pedido ya no está pendiente."}, status=status.HTTP_400_BAD_REQUEST)
        # Simulación de integración con pasarela de pago:
        # podría llamar a la API de un proveedor de pagos.
        #  pago  exitoso:
        pedido.estado = 'Pagado'
        pedido.save()
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_200_OK)
