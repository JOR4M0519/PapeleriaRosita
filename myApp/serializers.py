from rest_framework import serializers
from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra

#Realizar para cada tabla un serializer

#view set -> djanog convierte datos python en json & quien puede acceder a los datos

class UsuarioSerializer(serializers.UsuarioSerializer):
    class Meta:
        managed = True
        db_table = 'usuario'
        model = Usuario
        fields = ('id_usuario','username','nombre','telefono','num_identificacion','clave','rol','estado')
        #read_only_fields = ('cread_at')

class ProductoSerializer(serializers.ProductoSerializer):
    class Meta:
        managed = True
        db_table = 'producto'
        model = Producto
        fields = ('id_producto','nombre_producto','valor_compra','valor_venta','valor_ganancia','stock','estado')