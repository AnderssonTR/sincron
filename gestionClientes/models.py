from django.db import models

# Create your models here.
class GestionCliente(models.Model):
    gestionClienteRegistro=models.DateField(verbose_name='Fecha de registro',help_text='DD/MM/AAAA')
    gestionClienteObservacion=models.CharField(max_length=254,verbose_name='Descripción de gestion')
    gestionClienteTiempoInvertido=models.DecimalField(decimal_places=1,max_digits=2,verbose_name="tiempo de horas y fracción")

