
from .serializers import ArticuloSerializer,CategoriaSerializer
from .models import Articulo, Categoria
from rest_framework.permissions import AllowAny 
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class ArticuloViewSet(ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [AllowAny]


