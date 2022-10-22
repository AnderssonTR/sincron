from django.urls import path
from configuracion.views import estadoGestion, estadoGestion_crear, servicioOfrecido, servicioOfrecido_crear

urlpatterns = [
   path('servicioOfrecido/',servicioOfrecido,name='servicioOfrecido'),
   path('servicioOfrecido/crear/',servicioOfrecido_crear,name='servicioOfrecido-crear'),

   path('estadoGestion/',estadoGestion,name='estadoGestion'),
   path('estadoGestion/crear/',estadoGestion_crear,name='estadoGestion-crear'),
]