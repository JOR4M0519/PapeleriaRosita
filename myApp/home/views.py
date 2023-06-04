# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
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
            
            #Proveedores
            elif load_template == 'page-crte-proveedores.html':
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context,request))

            #Compras
            elif load_template == 'page-crte-compras.html':
                context['encabezado'] = 'Registrar Compra'
                return HttpResponse(html_template.render(context,request))
            
            #Ventas
            elif load_template == 'page-crte-ventas.html':
                context['encabezado'] = 'Registrar Venta'
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
                print(context['lista'])
                return HttpResponse(html_template.render(context,request))

            elif load_template == 'tables-productos.html':
                context['titulo_tabla'] = 'Productos'
                context['subtitulo_tabla'] = 'Lista detallada de los productos existentes en el inventario'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['columnas'] = ['Nombre del producto','Valor compra','Valor venta','Valor ganancia','Cantidad comprada','Estado']
                context['lista'] = json.loads(views.ProductoView().get(request).content)['products']
                return HttpResponse(html_template.render(context,request))

            return HttpResponse(html_template.render(context, request))

        #POST
        else:

          html_template = loader.get_template('home/' + load_template)

            #Productos
          if load_template == 'page-crte-product.html':

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

          elif load_template == 'tables-productos.html':
             
             if request.POST.get('id_eliminar')!=None:
                id_eliminar= request.POST.get('id_eliminar')
            
             elif request.POST.get('id_editar')!=None:
                id_product= request.POST.get('id_editar')

             return redirect(load_template)
            #Proveedores
          elif load_template == 'page-crte-proveedores.html':
            if request.POST.get('id_proveedor')==None:
                proveedor={'razon_social': request.POST['razon_social'],
                        'email_proveedor': request.POST['email_proveedor'],
                        'telefono': request.POST['telefono'],
                        'estado': 'A'}
                message = json.loads(views.ProveedorView.post(proveedor).content)
                context['result'] = message['message']
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context, request))  
            else:
                id_proveedor = request.POST.get('id_proveedor')
                return HttpResponse(html_template.render(context, request))  

            #Compras
          elif load_template == 'tables-compras.html':

            if request.POST.get('id_eliminar')!=None:
                id_eliminar= request.POST.get('id_eliminar')
                
            elif request.POST.get('id_editar')!=None:
                
                id_product= request.POST.get('id_editar')
                producto = json.loads(views.ProductoView.get(int(id_product)).content)
                
                context['result'] = ''
                context['encabezado'] = 'Editar producto'
                context['action'] = 'UPDATE'
                context['producto'] = producto
                html_template = loader.get_template('home/page-crte-product.html')
                return HttpResponse(html_template.render(context,request))
            
            elif request.POST.get('page_product_edit_button')!=None:
                
                id_producto = request.POST.get('id_producto')
                producto={'nombre_producto': request.POST['nombre_producto'],
                            'valor_compra': request.POST['valor_compra'],
                            'valor_venta': request.POST['valor_venta'],
                            'estado': request.POST['estado']}
                
                message = json.loads(views.ProductoView.put(producto,id_producto).content)
                print(message)
                #??
                #context['result'] = message['message']
                return HttpResponse(html_template.render(context, request))
            
            elif request.POST.get('boton_filtro')!=None:
                print('Generar reporte seleccionado')
            return redirect(load_template)
          
          





    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))