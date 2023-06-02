from rest_framework import routers
from django.urls import path
from .api import ProductoViewSet, UsuarioViewSet, ProveedorViewSet, DetallesVentaViewSet, DetallesCompraViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/productos',ProductoViewSet,'producto')
router.register('api/usuarios',UsuarioViewSet,'usuario')
router.register('api/proveedores',ProveedorViewSet,'proveedores')
router.register('api/detallesCompra',DetallesVentaViewSet,'detallesCompra')
router.register('api/detallesVenta',DetallesCompraViewSet,'detallesVenta')

urlpatterns = [
    # path('', views.index),
    path('producto/', views.ProductoView.as_view()),
    path('producto/<int:id>', views.ProductoView.as_view()),
    path('proveedor/', views.ProveedorView.as_view()),
    path('proveedor/<int:id>', views.ProveedorView.as_view())
]
urlpatterns += router.urls
