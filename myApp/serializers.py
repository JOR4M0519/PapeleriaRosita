from rest_framework import serializers
from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'telefono', 'num_identificacion', 'clave', 'rol', 'estado')

class ProveedorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('razon_social', 'email_proveedor', 'telefono', 'estado')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'valor_compra', 'valor_venta','valor_ganancia', 'stock', 'estado') 

class DetallesVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesVenta
        fields = ('id_producto', 'cantidad', 'fecha')
        read_only_fields = ('fecha',)

class DetallesCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesCompra
        fields = ('id_producto', 'id_proveedor', 'cantidad', 'fecha')
