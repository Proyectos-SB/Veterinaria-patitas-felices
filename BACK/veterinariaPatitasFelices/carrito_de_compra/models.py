from django.db import models
from articulos.models import Articulo
from usuarios.models import Cliente

class CarritoCompra(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f"Carrito de {self.cliente.usuario.email}"  

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE, related_name='items')
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)  # Evita que se eliminen artículos con ventas registradas
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.cantidad > self.articulo.stock:
            raise ValueError(f"Stock insuficiente para {self.articulo.nombre}. Solo hay {self.articulo.stock} unidades disponibles.")
        super().save(*args, **kwargs)

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
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_OPCIONES)
    estado = models.CharField(max_length=50, choices=ESTADO_OPCIONES, default='Pendiente')

    def calcular_total(self):
        return sum(item.cantidad * item.precio_unitario for item in self.items.all())

    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.cliente} - Total: ${self.total}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Guardar precio en el momento del pedido

    def __str__(self):
        return f"{self.cantidad} x {self.articulo.nombre} (Pedido {self.pedido.id})"