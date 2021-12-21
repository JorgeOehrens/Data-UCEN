from os import name
from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('transporte' , views.tipo_trasporte, name='tipo_trasporte'),
    path('pais' , views.pais , name='pais'),
    path('cantidad', views.cantidad , name='cantidad')
]
