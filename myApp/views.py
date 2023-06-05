import json
import psycopg2
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from mysite.settings import DATABASES 
from .models import Producto, Proveedor, DetallesVenta, DetallesCompra, Usuario, AuthUser
from .forms import login, signup


lista=[]
empleados=[]

def log_in(request):
    print('hello')
    if request.method == 'GET':
      return render(request, 'login.html',{
        'form': login()
      })
    else:
        
        lista.append({
           'nombreUsuario': request.POST['username'],
            'contrasena': request.POST['password'] })
        return redirect('login') #redirect('index')

def sign_up(request):
    if request.method == 'GET':
      return render(request, 'signup.html',{
        'form': signup()
      })
    else:
        empleados.append({
           'nombreEmpleado': request.POST['nombreEmpleado'],
            'edad': request.POST['edad'] })
        return redirect('index')

class ProductoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if (id > 0):
            products = list(Producto.objects.filter(id_producto=id).values())
            if len(products) > 0:
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

    def post(request):
        jd = (request)
        Producto.objects.create(nombre_producto=jd['nombre_producto'],
                                valor_compra=jd['valor_compra'],
                                valor_venta=jd['valor_venta'],
                                valor_ganancia=jd['valor_ganancia'],
                                stock=jd['stock'],
                                estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(producto, id):
        jd = producto
        products = list(Producto.objects.filter(id_producto=id).values())
        if len(products) > 0:
            product = Producto.objects.get(id_producto=id)
            product.nombre_producto = jd['nombre_producto']
            product.valor_compra = jd['valor_compra']
            product.valor_venta = jd['valor_venta']
            product.estado = jd['estado']
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
        if (id > 0):
            provider = list(Proveedor.objects.filter(id_proveedor=id).values())
            if len(provider) > 0:
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

    def post(request):
        jd = (request)
        Proveedor.objects.create(razon_social=jd['razon_social'],
                                 email_proveedor=jd['email_proveedor'],
                                 telefono=jd['telefono'],
                                 estado=jd['estado'])
        datos = {'message': ""}
        return JsonResponse(datos)

    def put(request, id):
        jd = json.loads(request.body)
        providers = list(Proveedor.objects.filter(id_proveedor=id).values())
        if len(providers) > 0:
            provider = Proveedor.objects.get(id_proveedor=id)
            provider.razon_social = jd['razon_social']
            provider.email_proveedor = jd['email_proveedor']
            provider.telefono = jd['telefono']
            provider.estado = jd['estado']
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


class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            user = list(AuthUser.objects.filter(id_usuario=id).values())
            if len(user) > 0:
                datos = {'message': "Success", 'user': user[0]}
            else:
                datos = {'message': "Usuario no Encontrado"}
        else:
            user = list(AuthUser.objects.values())
            if len(user) > 0:
                datos = {'message': "Success", 'users': user}
            else:
                datos = {'message': "No existen Usuarios"}

        return JsonResponse(datos)

    def post(request):
        jd = json.loads(request.body)
        AuthUser.objects.create(username=jd['username'],
                               nombre=jd['nombre'],
                               telefono=jd['telefono'],
                               num_identificacion=jd['num_identificacion'],
                               clave=jd['clave'],
                               rol=jd['rol'],
                               estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(request, id):
        jd = json.loads(request.body)
        details = list(AuthUser.objects.filter(id_usuario=id).values())
        if len(details) > 0:
            detail = AuthUser.objects.get(id_usuario=id)
            detail.username = jd['username']
            detail.nombre = jd['nombre']
            detail.telefono = jd['telefono']
            detail.num_identificacion = jd['num_identificacion']
            detail.clave = jd['clave']
            detail.rol = jd['rol']
            detail.estado = jd['estado']
            detail.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        details = list(AuthUser.objects.filter(id_usuario=id).values())
        if len(details) > 0:
            AuthUser.objects.filter(id_usuario=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no Encontrado"}
        return JsonResponse(datos)


class DetalleCompraView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        try:
            ps_connection = psycopg2.connect(user="postgres",
                                             password=DATABASES['default']['PASSWORD'],
                                             host="localhost",
                                             port="5432",
                                             database=DATABASES['default']['NAME'])
            cursor = ps_connection.cursor()
            if request['id_proveedor'] == 0:
                cursor.callproc('fn_reportecompra', [request['fecha_inicio'],request['fecha_final']])
            else:
                cursor.callproc('fn_reportecompraproveedor', [request['id_proveedor'],request['fecha_inicio'],request['fecha_final']])
            result = cursor.fetchone()
            if result[0] is not None:
                datos = {'message': 'Success', 'details': result[0]}
            else:
                datos = {'message': 'No se encontro ningun detalle'}

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            # closing database connection.
            if ps_connection:
                cursor.close()
                ps_connection.close()

        return JsonResponse(datos)

    def post(request):
        jd = (request)
        DetallesCompra.objects.create(id_producto_id=jd['id_producto'],
                                      id_proveedor_id=jd['id_proveedor'],
                                      cantidad=jd['cantidad'],
                                      fecha=jd['fecha'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(request, id):
        jd = json.loads(request.body)
        details = list(DetallesCompra.objects.filter(id_detcompra=id).values())
        if len(details) > 0:
            detail = DetallesCompra.objects.get(id_detcompra=id)
            detail.id_producto = jd['id_producto']
            detail.id_proveedor = jd['id_proveedor']
            detail.cantidad = jd['cantidad']
            detail.fecha = jd['fecha']
            detail.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        details = list(DetallesVenta.objects.filter(id_detcompra=id).values())
        if len(details) > 0:
            DetallesCompra.objects.filter(id_detcompra=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)


class DetalleVentaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        try:
            ps_connection = psycopg2.connect(user="postgres",
                                             password=DATABASES['default']['PASSWORD'],
                                             host="localhost",
                                             port="5432",
                                             database=DATABASES['default']['NAME'])
            cursor = ps_connection.cursor()
            if request['id_producto'] == 0:
                cursor.callproc('fn_reporteventa', [request['fecha_inicio'], request['fecha_final']])
            else:
                cursor.callproc('fn_reporteventaproducto', [request['id_proveedor'], request['fecha_inicio'], request['fecha_final']])
            result = cursor.fetchone()
            if result[0] is not None:
                datos = {'message': 'Success', 'details': result[0]}
            else:
                datos = {'message': 'No se encontro ningun detalle'}

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            # closing database connection.
            if ps_connection:
                cursor.close()
                ps_connection.close()

        return JsonResponse(datos)

    def post(request):
        jd = (request)
        DetallesVenta.objects.create(id_producto_id=jd['id_producto'],
                                     cantidad=jd['cantidad'],
                                     fecha=jd['fecha'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(request, id):
        jd = json.loads(request.body)
        details = list(DetallesVenta.objects.filter(id_detventa=id).values())
        if len(details) > 0:
            detail = DetallesCompra.objects.get(id_detventa=id)
            detail.id_producto = jd['id_producto']
            detail.cantidad = jd['cantidad']
            detail.fecha = jd['fecha']
            detail.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        details = list(DetallesVenta.objects.filter(id_detventa=id).values())
        if len(details) > 0:
            DetallesVenta.objects.filter(id_detventa=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)


class ReporteVentaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        jd = json.loads(request.body)
        if jd['id_producto'] == 0 and jd['fechaI'] == "0" and jd['fechaF'] == "0":
            details = list(DetallesVenta.objects.values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "No existen Detalles"}
        elif jd['fechaI'] == "0000-00-00" and jd['fechaF'] == "0000-00-00":
            details = list(
                DetallesVenta.objects.filter(id_producto=jd['id_producto']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['fechaF'] == "0":
            details = list(
                DetallesVenta.objects.filter(fecha__gte=jd['fechaI']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['fechaI'] == "0":
            details = list(
                DetallesVenta.objects.filter(fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['fechaF'] == "0":
            details = list(
                DetallesVenta.objects.filter(id_producto=jd['id_producto'], fecha__gte=jd['fechaI']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['fechaI'] == "0":
            details = list(
                DetallesVenta.objects.filter(id_producto=jd['id_producto'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0:
            details = list(
                DetallesVenta.objects.filter(fecha__gte=jd['fechaI'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        else:
            details = list(
                DetallesVenta.objects.filter(id_producto=jd['id_producto'], fecha__gte=jd['fechaI'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}

        return JsonResponse(datos)

class ReporteCompraView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        jd = json.loads(request.body)
        if jd['id_producto'] == 0 and jd['id_proveedor'] == 0 and jd['fechaI'] == "0" and jd['fechaF'] == "0":
            details = list(DetallesCompra.objects.values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "No existen Detalles"}
        elif jd['id_proveedor'] == 0 and jd['fechaI'] == "0" and jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_producto=jd['id_producto']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['fechaI'] == "0" and jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_proveedor=jd['id_proveedor']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['id_proveedor'] == 0 and jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(fecha__gte=jd['fechaI']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['id_proveedor'] == 0 and jd['fechaI'] == "0":
            details = list(
                DetallesCompra.objects.filter(fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['fechaI'] == "0" and jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_producto=jd['id_producto'], id_proveedor=jd['id_proveedor']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_proveedor'] == 0 and jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_producto=jd['id_producto'], fecha__gte=jd['fechaI']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_proveedor'] == 0 and jd['fechaI'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_producto=jd['id_producto'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_proveedor=jd['id_proveedor'], fecha__gte=jd['fechaI']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0 and jd['id_proveedor'] == 0:
            details = list(
                DetallesCompra.objects.filter(fecha__gte=jd['fechaI'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_producto'] == 0:
            details = list(
                DetallesCompra.objects.filter(id_proveedor=jd['id_proveedor'], fecha__gte=jd['fechaI'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['id_proveedor'] == 0:
            details = list(
                DetallesCompra.objects.filter(id_producto=jd['id_producto'], fecha__gte=jd['fechaI'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['fechaI'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_proveedor=jd['id_proveedor'], id_producto=jd['id_producto'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        elif jd['fechaF'] == "0":
            details = list(
                DetallesCompra.objects.filter(id_proveedor=jd['id_proveedor'], id_producto=jd['id_producto'], fecha__gte=jd['fechaI']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        else:
            details = list(
                DetallesCompra.objects.filter(id_proveedor=jd['id_proveedor'], id_producto=jd['id_producto'], fecha__gte=jd['fechaI'], fecha__lte=jd['fechaF']).values())
            if len(details) > 0:
                datos = {'message': "Success", 'details': details}
            else:
                datos = {'message': "Detalle no Encontrado"}
        return JsonResponse(datos)
