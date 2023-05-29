from django.contrib import admin
from .models import Usuario,Proveedor,Producto,DetallesVenta,DetallesCompra

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(DetallesVenta)
admin.site.register(DetallesCompra)

# Register your models here.