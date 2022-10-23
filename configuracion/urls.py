from django.urls import path
from configuracion.views import categoria, categoria_crear, estadoGestion, estadoGestion_crear, servicioOfrecido, servicioOfrecido_crear, subCategoria, subCategoria_crear

urlpatterns = [
   path('servicioOfrecido/',servicioOfrecido,name='servicioOfrecido'),
   path('servicioOfrecido/crear/',servicioOfrecido_crear,name='servicioOfrecido-crear'),

   path('estadoGestion/',estadoGestion,name='estadoGestion'),
   path('estadoGestion/crear/',estadoGestion_crear,name='estadoGestion-crear'),

   path('categoria/',categoria,name='categoria'),
   path('categoria/crear/',categoria_crear,name='categoria-crear'),

   path('subCategoria/',subCategoria,name='subCategoria'),
   path('subCategoria/crear/',subCategoria_crear,name='subCategoria-crear'),

   
]