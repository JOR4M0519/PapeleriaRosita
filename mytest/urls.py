from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('users/', views.get_users),
    path('create_product/', views.create_product)

]