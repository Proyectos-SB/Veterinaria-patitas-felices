from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, CarritoCompra, Pedido, ItemCarrito


def ver_carrito(request):
    cliente = get_object_or_404(Cliente, persona=request.user)
    
    # Intentamos obtener el carrito del cliente
    try:
        carrito = cliente.carrito
    except CarritoCompra.DoesNotExist:
        carrito = CarritoCompra.objects.create(cliente=cliente)

    # Calculamos el total del carrito
    total = sum(item.articulo.precio * item.cantidad for item in carrito.items.all())

    context = {
        'carrito': carrito,
        'total': total
    }
    return render(request, 'articulos/ver_carrito.html', context)


from django.views.decorators.http import require_POST

@require_POST
def modificar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    nueva_cantidad = int(request.POST.get('cantidad', 1))

    # Verificamos que no exceda el stock disponible
    if nueva_cantidad > item.articulo.stock:
        messages.error(request, "No hay suficiente stock.")
    else:
        item.cantidad = nueva_cantidad
        item.save()
    
    return redirect('articulos:ver_carrito')
def eliminar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    messages.success(request, "Artículo eliminado del carrito.")
    return redirect('articulos:ver_carrito')

def confirmar_pedido(request):
    cliente = get_object_or_404(Cliente, persona=request.user)

    # Verificamos si el cliente tiene un carrito activo
    try:
        carrito = cliente.carrito
    except CarritoCompra.DoesNotExist:
        messages.error(request, "No tenés un carrito de compras.")
        return redirect('articulos:lista_articulos')

    # Verificamos que el carrito tenga ítems
    if not carrito.items.exists():
        messages.error(request, "Tu carrito está vacío.")
        return redirect('articulos:lista_articulos')

    # Creamos un nuevo pedido
    nuevo_pedido = Pedido.objects.create(
        cliente=cliente,
        metodo_pago='Tarjeta'  
    )

    # Agregamos los ítems del carrito al pedido
    for item in carrito.items.all():
        # Verificamos que haya suficiente stock
        if item.cantidad > item.articulo.stock:
            messages.error(request, f"No hay suficiente stock de {item.articulo.nombre}.")
            return redirect('articulos:ver_carrito')
        
        nuevo_pedido.items.add(item)
        # Descontamos el stock
        item.articulo.stock -= item.cantidad
        item.articulo.save()

    # Guardamos el pedido con el total calculado
    nuevo_pedido.save()

    # Vaciamos el carrito después de confirmar el pedido
    carrito.items.all().delete()

    messages.success(request, "¡Pedido confirmado exitosamente!")
    return redirect('articulos:lista_pedidos')


def confirmar_pedido(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    carrito = cliente.carrito
    nuevo_pedido = Pedido.objects.create(cliente=cliente, metodo_pago='Tarjeta')

    for item in carrito.items.all():
        nuevo_pedido.items.add(item)

    nuevo_pedido.save()

    # Vaciar el carrito después de confirmar el pedido
    carrito.items.all().delete()

    return redirect('pedidos')



