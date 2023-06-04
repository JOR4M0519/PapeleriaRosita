# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect


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

            if load_template == 'admin':
                return HttpResponseRedirect(reverse('admin:index'))

            context['segment'] = load_template
            html_template = loader.get_template('home/' + load_template)
        
            if load_template == 'tables-compras.html':
                context['titulo_tabla'] = 'Compras'
                context['subtitulo_tabla'] = 'Lista detallada de compras realizadas'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['lista'] = [{'id':1,'producto':'Cocada','proveedor':'El mono','cantidad':10,'fecha':'10/5/231'},{'id':2,'producto':'Shampoo','proveedor':'La caspa','cantidad':12,'fecha':'10/5/231'},{'id':3,'producto':'Cocada','proveedor':'El mono','cantidad':10,'fecha':'10/5/231'},{'id':4,'producto':'Shampoo','proveedor':'La caspa','cantidad':12,'fecha':'11/5/231'}]
                return HttpResponse(html_template.render(context,request))

            elif load_template == 'tables-productos.html':
                context['titulo_tabla'] = 'Productos'
                context['subtitulo_tabla'] = 'Lista detallada de los productos existentes en el inventario'
                #Lista de JSON Ras - Mantener nombres de claves para que se haga la lista en el HTLM
                context['lista'] = [{'id':1,'producto':'Cocada','proveedor':'El mono','cantidad':10,'fecha':'10/5/231'},{'id':2,'producto':'Shampoo','proveedor':'La caspa','cantidad':12,'fecha':'10/5/231'},{'id':3,'producto':'Cocada','proveedor':'El mono','cantidad':10,'fecha':'10/5/231'},{'id':4,'producto':'Shampoo','proveedor':'La caspa','cantidad':12,'fecha':'11/5/231'}]
                return HttpResponse(html_template.render(context,request))

            return HttpResponse(html_template.render(context, request))   

        else:
    
            if load_template == 'tables-compras.html':
                id_eliminar= request.POST.get('id')
                print(id_eliminar)
                return redirect(load_template)

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
