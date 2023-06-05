# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .. import views
from django.shortcuts import redirect


@login_required(login_url="/login/")
def index(request):
    context = {}
    context ['segment']= 'index'
    context ['rol']= 'administrador'
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]

        if request.method == 'GET':
            
            #ADMIN
            if load_template == 'admin':
                return HttpResponseRedirect(reverse('admin:index'))
            
            context['action'] = 'GET'
            context['result'] = ''
            context['segment'] = load_template
            context ['rol']= 'administrador'
            html_template = loader.get_template('home/' + load_template)

            if load_template == 'page-user.html':
                html_template = loader.get_template('home/' + load_template)
                #views.UsuarioView.get

                return HttpResponse(html_template.render(context,request))

            #Productos
            if load_template == 'page-crte-product.html':
                context['encabezado'] = 'Agregar producto'
                return HttpResponse(html_template.render(context,request))
            
            elif load_template == 'tables-productos.html':
                context['titulo_tabla'] = 'Productos'
                context['subtitulo_tabla'] = 'Lista detallada de los productos existentes en el inventario'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['columnas'] = ['Nombre del producto','Nombre del proveedor','Cantidad comprada','Fecha']
                context['lista'] = json.loads(views.ProductoView().get(request).content)['products']
                return HttpResponse(html_template.render(context,request))

            #Proveedores
            elif load_template == 'tables-proveedores.html':
                context['titulo_tabla'] = 'Proveedor'
                context['subtitulo_tabla'] = 'Lista detallada de los proveedores existentes en el sistema'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['columnas'] = ['Razón social','Email','Teléfono','Estado']
                context['lista'] = json.loads(views.ProveedorView().get(request).content)['provider']
                return HttpResponse(html_template.render(context,request))


            elif load_template == 'page-crte-proveedores.html':
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context,request))

            #Compras
            elif load_template == 'page-crte-compras.html':
                context['encabezado'] = 'Registrar Compra'
                return HttpResponse(html_template.render(context,request))
            
            elif load_template == 'tables-compras.html':
                context['titulo_tabla'] = 'Compras'
                context['subtitulo_tabla'] = 'Lista detallada de compras realizadas'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['columnas'] = ['Nombre del producto','Nombre del proveedor','Cantidad comprada','Fecha']

                context['columnas_popu_provee'] = ['Razón social','Teléfono']
                
                context['lista_popu_provee'] = json.loads(views.ProveedorView().get(request).content)['provider']
                filtros = {
                    'id_proveedor': 0,
                    'fecha_inicio': '2023-01-30',
                    'fecha_final': '2023-06-30'
                }

                context['label_filtro'] = 'proveedores'

                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['lista'] = json.loads(views.DetalleCompraView().get(filtros).content)
                
                return HttpResponse(html_template.render(context,request))

            #ventas
            elif load_template == 'page-crte-ventas.html':
                context['encabezado'] = 'Registrar Venta'
                return HttpResponse(html_template.render(context,request))

            elif load_template == 'tables-productos.html':
                context['titulo_tabla'] = 'Productos'
                context['subtitulo_tabla'] = 'Lista detallada de los productos existentes en el inventario'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['columnas'] = ['Nombre del producto','Valor compra','Valor venta','Valor ganancia','Cantidad comprada','Estado']
                context['lista'] = json.loads(views.ProductoView().get(request).content)['products']
                return HttpResponse(html_template.render(context,request))

            elif load_template == 'tables-ventas.html':
                context['titulo_tabla'] = 'Ventas'
                context['subtitulo_tabla'] = 'Lista detallada de ventas realizadas'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['columnas'] = ['Nombre del producto','Cantidad vendida','Fecha']

                context['columnas_popu_provee'] = ['Razón social','Teléfono']
                
                context['lista_popu_provee'] = json.loads(views.ProveedorView().get(request).content)['provider']


                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['lista'] = [{'id_detventa':5,'nombre_producto': 'Peras','cantidad':100,'fecha':'3/6/2030'},{'id_detventa':10,'nombre_producto': 'piojos','cantidad':10000,'fecha':'3/6/2030'}]
                return HttpResponse(html_template.render(context,request))

            return HttpResponse(html_template.render(context, request))

        #POST
        else:

            html_template = loader.get_template('home/' + load_template)

                #***********
                #*Productos*
                #***********
            if load_template == 'tables-productos.html':
                #Eliminar
                if request.POST.get('id_eliminar')!=None:
                    id_eliminar= request.POST.get('id_eliminar')
                    return redirect(load_template)
                #Editar
                elif request.POST.get('id_editar')!=None:
                    
                    id_product= request.POST.get('id_editar')
                    producto = json.loads(views.ProductoView.get(views,request,id=int(id_product)).content)
                    
                    context['result'] = ''
                    context['encabezado'] = 'Editar producto'
                    context['action'] = 'UPDATE'
                    context['producto'] = producto
                    html_template = loader.get_template('home/page-crte-product.html')
                    return HttpResponse(html_template.render(context,request))
                #filtro
                elif request.POST.get('boton_filtro')!=None:
                    print('Generar reporte seleccionado')
                    return redirect(load_template)
                #Redirección para editar
                elif request.POST.get('page_product_edit_button')!=None:
                    
                    id_producto = request.POST.get('id_producto')
                    producto={'nombre_producto': request.POST['nombre_producto'],
                                'valor_compra': request.POST['valor_compra'],
                                'valor_venta': request.POST['valor_venta'],
                                'estado': request.POST['estado']}
                    message = json.loads(views.ProductoView.put(producto,id_producto).content)           
                    return redirect(load_template)
                
            if load_template == 'page-crte-product.html':
                #Crear Producto
                producto={'nombre_producto': request.POST['nombre_producto'],
                            'valor_compra': request.POST['valor_compra'],
                            'valor_venta': request.POST['valor_venta'],
                            'valor_ganancia': 0,
                            'stock': 0,
                            'estado': 'A'}
            
                message = json.loads(views.ProductoView.post(producto).content)
                context['result'] = message['message']
                context['encabezado'] = 'Agregar producto'
                return HttpResponse(html_template.render(context, request))
            
                #*************
                #*Proveedores*
                #*************
            elif load_template == 'page-crte-proveedores.html':
                #Crear Proveedor
                proveedor={ 'razon_social': request.POST['razon_social'],
                            'email_proveedor': request.POST['email_proveedor'],
                            'telefono': request.POST['telefono'],
                            'estado': 'A'}
                message = json.loads(views.ProveedorView.post(proveedor).content)
                context['result'] = message['message']
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context, request))  
            
            if load_template == 'tables-proveedores.html':
                #Eliminar
                if request.POST.get('id_eliminar')!=None:
                    id_eliminar= request.POST.get('id_eliminar')
                    return redirect(load_template)
                #Editar
                elif request.POST.get('id_editar')!=None:
                    
                    id_proveedor= request.POST.get('id_editar')
                    proveedor = json.loads(views.ProveedorView.get(views,request,id=int(id_proveedor)).content)
                    
                    context['result'] = ''
                    context['encabezado'] = 'Editar Proveedor'
                    context['action'] = 'UPDATE'
                    context['proveedor'] = proveedor
                    html_template = loader.get_template('home/page-crte-proveedores.html')
                    return HttpResponse(html_template.render(context,request))
                #filtro
                elif request.POST.get('boton_filtro')!=None:
                    
                    return redirect(load_template)
                #Redirección para editar
                elif request.POST.get('page_proveedor_edit_button')!=None:
                    
                    id_proveedor = request.POST.get('id_proveedor')
                    proveedor={'razon_social': request.POST['razon_social'],
                                'email_proveedor': request.POST['email_proveedor'],
                                'telefono': request.POST['telefono'],
                                'estado': request.POST['estado']}
                    message = json.loads(views.ProveedorView.put(proveedor,id_proveedor).content)           
                    return redirect(load_template)


                #*********
                #*Compras*
                #*********
            if load_template == 'page-crte-compras.html':
                #Crear compra
                compra={'cantidad': request.POST['cantidad'],
                            'fecha': request.POST['fecha'],
                            'id_producto': request.POST['id_producto'],
                            'id_proveedor': request.POST['id_proveedor']}
                
                message = json.loads(views.DetalleCompraView.post(compra).content)
                context['result'] = message['message']
                context['encabezado'] = 'Registrar Compra'
                return HttpResponse(html_template.render(context, request))
            
            elif load_template == 'tables-compras.html':
                #Eliminar
                if request.POST.get('id_eliminar')!=None:
                    id_eliminar= request.POST.get('id_eliminar')
                #Editar
                elif request.POST.get('id_editar')!=None:
                    
                    id_product= request.POST.get('id_editar')
                    producto = json.loads(views.DetalleCompraView.get(int(id_product)).content)
                    
                    context['result'] = ''
                    context['encabezado'] = 'Editar producto'
                    context['action'] = 'UPDATE'
                    context['producto'] = producto
                    html_template = loader.get_template('home/page-crte-product.html')
                    return HttpResponse(html_template.render(context,request))
                #Redirección para editar
                elif request.POST.get('page_product_edit_button')!=None:
                    
                    id_producto = request.POST.get('id_producto')
                    producto={'nombre_producto': request.POST['nombre_producto'],
                                'valor_compra': request.POST['valor_compra'],
                                'valor_venta': request.POST['valor_venta'],
                                'estado': request.POST['estado']}
                    
                    message = json.loads(views.ProductoView.put(producto,id_producto).content)           
                    return HttpResponse(html_template.render(context, request))
                #filtro
                elif request.POST.get('boton_filtro')!=None:
                    print('Generar reporte seleccionado')
                    return redirect(load_template)
                #Crear Compra
                else:
                    compra={'id_proveedor': request.POST['nombre_producto'],
                        'id_producto': request.POST['valor_compra'],
                        'fecha': request.POST['valor_venta'],
                        'cantidad': 0}
                    
                    message = json.loads(views.DetalleCompraView.post(compra).content)
                    context['result'] = message['message']
                    context['encabezado'] = 'Registrar Compra'
                    return HttpResponse(html_template.render(context, request))
                
            #**********
            #**Ventas**
            #**********
            if load_template == 'page-crte-ventas.html':
            #Crear Ventas
                date = datetime.now()
                date = date.strftime("%Y-%m-%d")

                venta={    'cantidad': request.POST['cantidad'],
                            'id_producto': request.POST['id_producto'],
                            'fecha': date}
                print(venta)
                message = json.loads(views.DetalleVentaView.post(venta).content)
                context['result'] = message['message']
                context['encabezado'] = 'Registrar Venta'
                return HttpResponse(html_template.render(context, request))
                
            return redirect(load_template)

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))