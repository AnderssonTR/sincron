from django.urls import path
from configuracion.views import servicioOfrecido, servicioOfrecido_crear

urlpatterns = [
   path('servicioOfrecido/',servicioOfrecido,name='servicioOfrecido'),
   path('servicioOfrecido/crear/',servicioOfrecido_crear,name='servicioOfrecido-crear'),
]