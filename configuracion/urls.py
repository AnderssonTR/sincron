from django.urls import path
from configuracion.views import configuracion

urlpatterns = [
   path('',configuracion,name='configuracion'),
]