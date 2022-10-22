from django  import forms

from configuracion.models import EstadoGestion, ServicioOfrecido

# Formulario de servicio ofrecido
class ServicioOfrecidoForm(forms.ModelForm):
    class Meta:
        model=ServicioOfrecido
        #fields='__all__'
        exclude=['servicioOfrecidoActivo']


# Formulario de estado de gestion
class EstadoGesionForm(forms.ModelForm):
    class Meta:
        model=EstadoGestion
        #fields='__all__'
        exclude=['estadoGestionActivo']