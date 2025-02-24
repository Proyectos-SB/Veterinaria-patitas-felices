from django.db import models

# Create your models here.



class Categoria(models.Model):
    
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    

    


class Articulo(models.Model):
    
    id_articulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    tipo_mascota = models.ForeignKey('models.TipoMascota', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nombre
        