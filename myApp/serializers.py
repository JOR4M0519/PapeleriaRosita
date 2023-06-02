from rest_framework import serializers
from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra

#Realizar para cada tabla un serializer

#view set -> djanog convierte datos python en json & quien puede acceder a los datos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario','username','nombre','telefono','num_identificacion','clave','rol','estado')
        #read_only_fields = ('cread_at')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id_producto','nombre_producto','valor_compra','valor_venta','valor_ganancia','stock','estado')