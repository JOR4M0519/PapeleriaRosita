from rest_framework import routers
from django.urls import path, include
from .views import ProductoView

urlpatterns = [
    # path('', views.index),
    path('producto/', ProductoView.as_view()),
    path('producto/<int:id>', ProductoView.as_view())
]