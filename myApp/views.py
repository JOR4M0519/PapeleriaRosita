from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import login, signup

lista=[]
empleados=[]

def index(request):
    return render(request, 'index.html',{
        'listaUsuario': lista
    })


def sign_up(request):
    return render(request, 'signup.html')

def log_in(request):
    if request.method == 'GET':
      return render(request, 'login.html',{
        'form': login()
      })
    else:
        lista.append({
           'nombreUsuario': request.POST['username'],
            'contrasena': request.POST['password'] })
        return redirect('index')

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