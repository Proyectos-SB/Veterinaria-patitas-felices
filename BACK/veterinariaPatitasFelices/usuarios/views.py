from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ClienteRegistroSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import update_session_auth_hash


class ClienteRegistroAPIView(APIView):
    def post(self, request):
        serializer = ClienteRegistroSerializer(data=request.data)
        if serializer.is_valid():
            usuario  = serializer.save()
            return Response({
                "message": "Cliente registrado con éxito",
                "cliente": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user:
                # Generar el token JWT
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                })
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ObtenerUsuarioAutenticadoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Obtener los datos del usuario autenticado.
        """
        usuario = request.user  # Obtiene el usuario autenticado
        serializer = ClienteRegistroSerializer(usuario)  # Serializa los datos del usuario
        return Response(serializer.data)

class ActualizarUsuarioAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        """
        Actualizar los datos del usuario autenticado.
        """
        usuario = request.user  # Obtiene el usuario autenticado
        serializer = ClienteRegistroSerializer(usuario, data=request.data, partial=True)  # Usa partial=True para permitir actualizaciones parciales

        if serializer.is_valid():
            serializer.save()  # Guarda los cambios
            # Si se actualizó la contraseña, actualiza la sesión del usuario
            if 'password' in request.data:
                update_session_auth_hash(request, usuario)  # Esto evita que el usuario se desconecte después de cambiar su contraseña
            return Response({
                "message": "Usuario actualizado correctamente.",
                "usuario": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  