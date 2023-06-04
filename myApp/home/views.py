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

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
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

            context['segment'] = load_template
            html_template = loader.get_template('home/' + load_template)

            #Productos
            if load_template == 'page-crte-product.html':
                context['message'] = ''
                context['encabezado'] = 'Agregar producto'
                return HttpResponse(html_template.render(context,request))
            
            #Proveedores
            if load_template == 'page-crte-proveedores.html':
                context['message'] = ''
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context,request))

            #Compras
            if load_template == 'page-crte-proveedores.html':
                context['message'] = ''
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context,request))
            
            #Ventas
            if load_template == 'page-crte-proveedores.html':
                context['message'] = ''
                context['encabezado'] = 'Agregar Proveedor'
                return HttpResponse(html_template.render(context,request))
            

            return HttpResponse(html_template.render(context, request))

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
            context['message'] = message['message']
            context['encabezado'] = 'Agregar producto'
            return HttpResponse(html_template.render(context, request))
            
            #Proveedores
          if load_template == 'page-crte-proveedores.html':
            proveedor={'razon_social': request.POST['razon_social'],
                      'email_proveedor': request.POST['email_proveedor'],
                      'telefono': request.POST['telefono'],
                      'estado': 'A'}
            message = json.loads(views.ProveedorView.post(proveedor).content)
            context['message'] = message['message']
            context['encabezado'] = 'Agregar Proveedor'
            return HttpResponse(html_template.render(context, request))  

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))