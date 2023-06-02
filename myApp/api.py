from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra
from rest_framework import viewsets, permissions

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = 
