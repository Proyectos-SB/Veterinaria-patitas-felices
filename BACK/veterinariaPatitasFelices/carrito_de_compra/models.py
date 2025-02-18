from django.db import models
from articulos.models import Articulo
from usuarios.models import Cliente
# Create your models here.

class CarritoCompra(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f"Carrito de {self.cliente.persona.email}"  # Usar email para más claridad

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE, related_name='items')
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.articulo.nombre}"

class Pedido(models.Model):
    ESTADO_OPCIONES = [
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    METODO_PAGO_OPCIONES = [
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
        ('Efectivo', 'Efectivo'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.SET_NULL, null=True, blank=True)  # Para mantener historial del carrito
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_OPCIONES)
    estado = models.CharField(max_length=50, choices=ESTADO_OPCIONES, default='Pendiente')

    def __str__(self):
        return f"Pedido de {self.cliente.persona.email} - Total: ${self.total}"