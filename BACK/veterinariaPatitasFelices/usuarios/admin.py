from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import Persona, Medico, Cliente


admin.site.register(Medico)
admin.site.register(Cliente)

class PersonaAdmin(admin.ModelAdmin):
   
    
   
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'dni', 'fecha_nacimiento')
        }),
        ('Datos de Contacto', {
            'fields': ('direccion', 'telefono')
        }),
        ('Roles', {
            'fields': ('is_cliente', 'is_veterinario', 'is_administrador_limitado')
        }),
    )
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'dni', 'is_cliente', 'is_veterinario')



class PersonaAdmin(UserAdmin):
    # Configuración de los campos en la vista de edición del usuario
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'dni')
        }),
        ('Datos de Contacto', {
            'fields': ('direccion', 'telefono')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Roles Especiales', {
            'fields': ('is_cliente', 'is_veterinario', 'is_administrador_limitado')
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    # Configuración de los campos en la vista de creación de un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'dni',
                'direccion', 'telefono', 'password1', 'password2', 
                'is_cliente', 'is_veterinario', 'is_administrador_limitado'
            ),
        }),
    )
    
    # Campos que se muestran en la lista de usuarios
    list_display = (
        'email', 'username', 'first_name', 'last_name', 'dni', 
        'is_staff', 'is_cliente', 'is_veterinario', 'is_administrador_limitado'
    )
    
    # Campos por los que se puede buscar
    search_fields = ('email', 'username', 'first_name', 'last_name', 'dni')    

admin.site.register(Persona, PersonaAdmin)