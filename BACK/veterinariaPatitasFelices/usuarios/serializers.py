from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class ClienteRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 
            'last_name', 'direccion', 'telefono', 
            'password', 'is_cliente'
        ]
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            direccion=validated_data['direccion'],
            telefono=validated_data['telefono'],
            password=validated_data['password']
        )
        user.is_cliente = True  # Se marca como cliente
        user.save()
        # El método save() del modelo Usuario se encargará de crear el registro en Cliente
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()