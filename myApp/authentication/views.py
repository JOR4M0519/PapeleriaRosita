# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .. import views

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credenciales invalidas'
        else:
            msg = 'Error en los campos digitados'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
def register_user(request):
    msg = None
    success = None

    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            success = False
            msg = 'Error de formulario'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def register_user2(request):
    msg = None
    success = False
    if request.method == "GET":
        return render(request, "accounts/register.html")
    else:
        usuario={'nombre_producto': request.POST['password1'],
            'valor_compra': request.POST['valor_compra'],
            'valor_venta': request.POST['valor_venta'],
            'valor_ganancia': 0,
            'stock': 0,
            'estado': 'A'}

        return render(request, "accounts/register.html")
    # if request.method == "POST":
        
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get("username")
    #         raw_password = form.cleaned_data.get("password1")
    #         user = authenticate(username=username, password=raw_password)

    #         msg = 'Usuario creado - please <a href="/login">login</a>.'
    #         success = True

    #         return redirect("/login/")

    #     else:
    #         msg = 'Error en los campos digitados'
    # else:
    #     form = SignUpForm()

    
