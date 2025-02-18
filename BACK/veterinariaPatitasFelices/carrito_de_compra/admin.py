from django.contrib import admin
from carrito_de_compra.models import CarritoCompra, ItemCarrito, Pedido

admin.site.register(CarritoCompra)
admin.site.register(ItemCarrito)
admin.site.register(Pedido)
# Register your models here.
