from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer,ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Proveedor

class DetallesVentaViewSet(viewsets.ModelViewSet):
    queryset = DetallesVenta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallesVenta

class DetallesCompraViewSet(viewsets.ModelViewSet):
    queryset = DetallesCompra.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallesCompra