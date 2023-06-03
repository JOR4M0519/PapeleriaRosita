from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
#from myApp.models import AuthUser, Producto 
from django.shortcuts import get_object_or_404, render
from .forms import CreateProduct

# Create your views here.
def hello(request):
    shello = 1
    return HttpResponse('<h1>Hello World %s</h1>' % shello)

def index(request):
    return render(request, 'index.html')

def about(request):
    title = 'Titular Acerca de'
    variable = 'USUARIOS:'
    #users = .objects.all()
    #users = {nombre:'hernan',edad:5}

    return render(request, 'about.html', {
        'title' : title,
        'variable': variable,
        'users': "ala"
    })

def create_product(request):
    if request.method == 'GET':    
        return render(request, 'create_product.html',{
            'form': CreateProduct()
        })
    else:
        print(request.GET)
        return redirect('/create_product/')
        #Producto.objects.create(nombre_producto=request.GET['nombre_producto'])

def get_users(request):
    #usersM = list(AuthUser.objects.values())
    #user = AuthUser.objects.get(title='usuario') 
    #user = get_object_or_404(AuthUser,id=101)
    #return JsonResponse(usersM, safe=False)
    return "Hello"