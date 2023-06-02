from rest_framework import routers
from django.urls import path
from .api import ProductoViewSet, UsuarioViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/productos',ProductoViewSet,'producto')
router.register('api/usuarios',UsuarioViewSet,'usuario')

urlpatterns = [
    # path('', views.index),
    path('producto/', views.ProductoView.as_view()),
    path('producto/<int:id>', views.ProductoView.as_view())
]

urlpatterns += router.urls