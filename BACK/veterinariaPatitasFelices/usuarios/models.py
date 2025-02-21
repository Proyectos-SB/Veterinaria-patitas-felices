from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager , PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)






class Persona(AbstractUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=8, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    is_cliente = models.BooleanField(default=False)
    is_veterinario = models.BooleanField(default=False) 
    is_administrador_limitado = models.BooleanField(default=False) 


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Asociar con Cliente si es cliente
        if self.is_cliente:
            Cliente.objects.get_or_create(persona=self)
        else:
            Cliente.objects.filter(persona=self).delete()
        
        # Asociar con Veterinario si es cliente
        if self.is_veterinario:
            Veterinario.objects.get_or_create(persona=self)
        else:
            Veterinario.objects.filter(persona=self).delete()
            
    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
        

             
class Cliente(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return f"Cliente: {self.persona.first_name} {self.persona.last_name}"


class Veterinario(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='veterinario')
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Dr. {self.persona.first_name} {self.persona.last_name}"
    
class Administradorlimitado(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='administrador_limitado')
    
    def __str__(self):
        return f"Administrador limitado: {self.persona.first_name} {self.persona.last_name}"