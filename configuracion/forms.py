from django  import forms

from configuracion.models import Categoria, EstadoGestion, ServicioOfrecido, SubCategoria

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

# Formulario de categorias
class CategoriasForm(forms.ModelForm):
    class Meta:
        model=Categoria
        #fields='__all__'
        exclude=['categoriaActivo']

# Formulario de sub-categorias
class SubCategoriasForm(forms.ModelForm):
    class Meta:
        model=SubCategoria
        #fields='__all__'
        exclude=['subCategoriaActivo']