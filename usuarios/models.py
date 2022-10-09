from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
class Usuario(models.Model):
    usuarioNombre=models.CharField(max_length=45, verbose_name="Nombre")
    usuarioApellido=models.CharField(max_length=45, verbose_name="Apellidos")
    class TipoDocumento(models.Model):
        CC='CC',_('Cédula de cuidadanía')
        CE='CE',_('Cédula extranjera')
        PP='PP',_('Pasaporte')
        TI='TI',_('Tarjeta de identidad')
        RC='RC',_('Registro civil')
    usuarioTipoDocumento=models.CharField (max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    usuarioNumeroDocumento=models.CharField(max_length =50, verbose_name ="Numero de documento")
    #usuarioClave=models.CharField(max_length=45,verbose_name="Contraseña")
    usuarioCorreo=models.CharField(max_length=55,verbose_name="Correo electrónico")
    class Rol(models.Model):
        comercial='Comercial',_('Comercial')
        mercadeo='Mercadeo',_('Mercadeo')
        administrador='Administrador',_('Administrador')
        soporte='Soporte',_('Soporte')
    usarioRol=models.CharField(max_length=15, choices=Rol.choices, default=Rol.mercadeo, verbose_name="Rol de usuario")
    class Estado(models.Model):
        activo='1',_('Activo')
        inactivo='0',_('Inactivo')
    usuarioActivo=models.CharField(max_length=1,choices=Estado.choises, default=Estado.activo, verbose_name="Estado" )


class Auditoria(models.Model):
    auditoriaNombre=models.CharField(max_length=45, verbose_name="Nombre")
    auditoriaDescripcion=models.CharField(max_length=255, verbose_name="Descripción")
    auditoriaRegistro=models.DateField(verbose_name='Fecha de registro')
    auditoriaIdUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name="Usuario")
    auditoriaIdGestionCliente=models.ForeignKey('GestionCliente', on_delete=models.CASCADE,verbose_name="Gestion cliente")

class MonitorEstado(models.Model):
    class Periodo(models.Model):
        semana='SEMANA',_('Semana')
        mes='MES',_('Mes')
    monitorEstadoPeriodo=models.CharField(max_length=10,choices=Periodo.choises, default=Periodo.semana, verbose_name="Periodo de tiempo")
    monitorEstadoMeta=models.CharField(max_length=3,verbose_name="Meta de gestion")
    monitorEstadoValor=models.CharField(max_length=4,verbose_name="Valor porcentual de gestion")
    monitorEstadoDescripcion=models.CharField(max_length=45,verbose_name="Descripcion de monitor de estado")
    class Estado(models.Model):
        activo='1',_('Activo')
        inactivo='0',_('Inactivo')
    monitorEstadoActivo=models.CharField(max_length=1,choices=Estado.choises, default=Estado.activo, verbose_name="Estado" )
    monitorEstadoIdUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name="Usuario")




