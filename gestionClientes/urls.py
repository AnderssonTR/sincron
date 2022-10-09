from django.urls import path
from gestionClientes.views import gestionClientes

urlpatterns = [
    path('',gestionClientes,name='gestionClientes'),
]