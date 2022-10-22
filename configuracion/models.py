from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
# Modelamiento de servicio ofrecido
class ServicioOfrecido(models.Model):
    servicioOfrecidoNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    servicioOfrecidoDesripcion = models.CharField(max_length= 125,verbose_name='Descripción')
    class Estado(models.TextChoices):
        activo='1',_('Activo')
        inactivo='0',_('Inactivo')
    servicioOfrecidoActivo=models.CharField(max_length=1,choices=Estado.choices, default=Estado.activo, verbose_name="Estado" )


# Modelamiento de estado de gestión
class EstadoGestion(models.Model):
    estadoGestionNombre=models.CharField(max_length=45, verbose_name='Nombre')
    estadoGestionDescripcion=models.CharField(max_length=125, verbose_name='Descripción')
    class Estado(models.TextChoices):
        activo='1',_('Activo')
        inactivo='0',_('Inactivo')
    estadoGestionActivo=models.CharField(max_length=1,choices=Estado.choices,default=Estado.activo, verbose_name='Estado')
