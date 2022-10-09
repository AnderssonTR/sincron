from django  import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        #fields='__all__'
        exclude=['usuarioActivo']