from rest_framework import serializers
from articulos.models import Articulo
from .models import CarritoCompra, ItemCarrito, Pedido, ItemPedido

# Serializador para el Artículo (datos básicos)
class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id_articulo', 'nombre', 'descripcion', 'precio', 'stock']

# Serializador para el Item del Carrito
class ItemCarritoSerializer(serializers.ModelSerializer):
    articulo = ArticuloSerializer(read_only=True)
    articulo_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ItemCarrito
        fields = ['id', 'articulo', 'articulo_id', 'cantidad']

    def validate(self, data):
        # Validar que la cantidad no exceda el stock del artículo
        articulo_id = data.get('articulo_id')
        cantidad = data.get('cantidad')
        try:
            articulo = Articulo.objects.get(id_articulo=articulo_id)
        except Articulo.DoesNotExist:
            raise serializers.ValidationError("El artículo no existe.")
        if cantidad > articulo.stock:
            raise serializers.ValidationError(f"Stock insuficiente para {articulo.nombre}. Solo hay {articulo.stock} unidades disponibles.")
        return data

    def create(self, validated_data):
        articulo_id = validated_data.pop('articulo_id')
        articulo = Articulo.objects.get(id_articulo=articulo_id)
        return ItemCarrito.objects.create(articulo=articulo, **validated_data)

# Serializador para el Carrito de Compra
class CarritoCompraSerializer(serializers.ModelSerializer):
    items = ItemCarritoSerializer(many=True, read_only=True)

    class Meta:
        model = CarritoCompra
        fields = ['id', 'cliente', 'items']
        read_only_fields = ['cliente']

# Serializador para el Item del Pedido
class ItemPedidoSerializer(serializers.ModelSerializer):
    articulo = ArticuloSerializer(read_only=True)

    class Meta:
        model = ItemPedido
        fields = ['id', 'articulo', 'cantidad', 'precio_unitario']

# Serializador para el Pedido
class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'total', 'fecha_pedido', 'metodo_pago', 'estado', 'items']
        read_only_fields = ['cliente', 'total', 'fecha_pedido', 'estado']