from rest_framework import serializers
from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra

#Realizar para cada tabla un serializer

#view set -> djanog convierte datos python en json & quien puede acceder a los datos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'telefono', 'num_identificacion', 'clave', 'rol', 'estado') 
        read_only_fields = ('created_at',)

class ProveedorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('razon_social', 'email_proveedor', 'telefono', 'estado')
        read_only_fields = ('created_at',)

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')
        read_only_fields = ('created_at',)

class DetallesVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesVenta
        fields = ('id_producto', 'cantidad', 'fecha')
        read_only_fields = ('fecha',)

class DetallesCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesCompra
        fields = ('id_producto', 'id_proveedor', 'cantidad', 'fecha')
        read_only_fields = ('created_at',)
