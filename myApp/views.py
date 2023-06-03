import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Producto, Proveedor, DetallesVenta
from .forms import CreateProduct


# Create your views here.

# def index(request):
#     return render(request, 'index.html')
#
# def index(request):
#     return render(request, 'proveedor.html')

class ProductoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            products = list(Producto.objects.filter(id_producto=id).values())
            if len(products)>0:
                datos = {'message': "Success", 'product': products[0]}
            else:
                datos = {'message': "Producto no Encontrado"}
        else:
            products = list(Producto.objects.values())
            if len(products) > 0:
                datos = {'message': "Success", 'products': products}
            else:
                datos = {'message': "No existen Productos"}

        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Producto.objects.create(nombre_producto=jd['nombre_producto'],
                                valor_compra=jd['valor_compra'],
                                valor_venta=jd['valor_venta'],
                                valor_ganancia=jd['valor_ganancia'],
                                stock=jd['stock'],
                                estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        products = list(Producto.objects.filter(id_producto=id).values())
        if len(products)>0:
            product = Producto.objects.get(id_producto=id)
            product.nombre_producto=jd['nombre_producto']
            product.valor_compra=jd['valor_compra']
            product.valor_venta=jd['valor_venta']
            product.valor_ganancia=jd['valor_ganancia']
            product.stock=jd['stock']
            product.estado=jd['estado']
            product.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Producto no Encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        products = list(Producto.objects.filter(id_producto=id).values())
        if len(products) > 0:
            Producto.objects.filter(id_producto=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Producto no Encontrado"}
        return JsonResponse(datos)

class ProveedorView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            provider = list(Proveedor.objects.filter(id_proveedor=id).values())
            if len(provider)>0:
                datos = {'message': "Success", 'provider': provider[0]}
            else:
                datos = {'message': "Proveedor no Encontrado"}
        else:
            provider = list(Proveedor.objects.values())
            if len(provider) > 0:
                datos = {'message': "Success", 'provider': provider}
            else:
                datos = {'message': "No existen Proveedores"}

        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Proveedor.objects.create(razon_social=jd['razon_social'],
                                email_proveedor=jd['email_proveedor'],
                                telefono=jd['telefono'],
                                estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        providers = list(Proveedor.objects.filter(id_proveedor=id).values())
        if len(providers)>0:
            provider = Proveedor.objects.get(id_proveedor=id)
            provider.razon_social=jd['razon_social']
            provider.email_proveedor=jd['email_proveedor']
            provider.telefono=jd['telefono']
            provider.estado=jd['estado']
            provider.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Proveedor no Encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        providers = list(Proveedor.objects.filter(id_proveedor=id).values())
        if len(providers) > 0:
            Proveedor.objects.filter(id_proveedor=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Proveedor no Encontrado"}
        return JsonResponse(datos)

class DetalleVentaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            details = list(DetallesVenta.objects.filter(id_detventa=id).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details[0]}
            else:
                datos = {'message': "Detalle no Encontrado"}
        else:
            details = list(DetallesVenta.objects.values())
            if len(details) > 0:
                datos = {'message': "Success", 'provider': details}
            else:
                datos = {'message': "No existen Detalles"}

        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        DetallesVenta.objects.create(id_producto=jd['id_producto'],
                                cantidad=jd['cantidad'],
                                fecha=jd['fecha'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        details = list(DetallesVenta.objects.filter(id_detventa=id).values())
        if len(details)>0:
            detail = DetallesVenta.objects.get(id_detventa=id)
            detail.id_producto=jd['id_producto']
            detail.cantidad=jd['cantidad']
            detail.fecha=jd['fecha']
            detail.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        details = list(DetallesVenta.objects.filter(id_detventa=id).values())
        if len(details) > 0:
            Proveedor.objects.filter(id_detventa=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Proveedor no Encontrado"}
        return JsonResponse(datos)
