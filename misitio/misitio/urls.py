"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from biblioteca import views
from django.urls import path
from contactos.views import contacto
from . import view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('hola/', view.hola, name='hola'),
    path('fecha/', view.fecha_actual, name='fecha'),
    path('fecha/mas/<int:offset>', view.horas_adelante, name='horas_adelante'),
    path('atributos_meta/', view.atributos_meta, name='atributos_meta'),
    path('buscar/', views.buscar, name='buscar'),
    path('contacto/', contacto, name='contacto'),
]
