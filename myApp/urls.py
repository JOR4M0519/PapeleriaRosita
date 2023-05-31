from rest_framework import routers
from django.urls import path
from . import views

router = routers.DeultRouter()

urlpatterns = [
    path('', views.index),
]