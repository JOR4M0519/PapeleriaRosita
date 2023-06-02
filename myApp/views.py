import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Producto
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
