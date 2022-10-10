from django  import forms

from configuracion.models import ServicioOfrecido

class ServicioOfrecidoForm(forms.ModelForm):
    class Meta:
        model=ServicioOfrecido
        #fields='__all__'
        exclude=['servicioOfrecidoActivo']