from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'products', views.ArticuloViewSet)

urlpatterns = router.urls