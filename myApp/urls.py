from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sigup/', views.sign_up, name='sigup'),
    path('login/', views.log_in, name='login')
]