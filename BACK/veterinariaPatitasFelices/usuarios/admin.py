from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import Usuario, Veterinario, Cliente


admin.site.register(Veterinario)
admin.site.register(Cliente)

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'fecha_nacimiento')}),
        ('Datos de Contacto', {'fields': ('direccion', 'telefono')}),
        ('Roles', {'fields': ('is_cliente', 'is_veterinario', 'is_administrador_limitado')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 
                'direccion', 'telefono', 'password1', 'password2', 
                'is_cliente', 'is_veterinario', 'is_administrador_limitado'
            ),
        }),
    )

    list_display = ('email', 'username', 'first_name', 'last_name', 
                    'is_staff', 'is_cliente', 'is_veterinario', 'is_administrador_limitado')
    
    search_fields = ('email', 'username', 'first_name', 'last_name')    

admin.site.register(Usuario, UsuarioAdmin)