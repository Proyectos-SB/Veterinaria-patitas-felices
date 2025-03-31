
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/articulos/', include('articulos.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/mascotas/', include('mascotas.urls')),
    path('api/carrito/', include('carrito_de_compra.urls')),
    path('api/vacunas/', include('vacunas.urls')),
     
]
