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

# Modelamiento de categoria
class Categoria(models.Model):
    categoriaDescripcion=models.CharField(max_length=45, verbose_name='Descripción')
    class Estado(models.TextChoices):
        activo='1',_('Activo')
        inactivo='0',_('Inactivo')
    categoriaActivo=models.CharField(max_length=1,choices=Estado.choices,default=Estado.activo, verbose_name='Estado')
    def __str__(self)->str:
        return "%s" %(self.categoriaDescripcion)  


# Modelamiento de subcategoria
class SubCategoria(models.Model):
    subCategoriaDescripcion=models.CharField(max_length=45, verbose_name='Descripción')
    class Estado(models.TextChoices):
        activo='1',_('Activo')
        inactivo='0',_('Inactivo')
    subCategoriaActivo=models.CharField(max_length=1,choices=Estado.choices,default=Estado.activo, verbose_name='Estado')
    categoria_idCategoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False,null=True, verbose_name="Categoria")

