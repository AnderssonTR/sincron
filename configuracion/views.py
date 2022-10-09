from django.shortcuts import render

# Create your views here.
def configuracion(request):
    titulo='Configuracion'
    context={
        'titulo':titulo,
    }
    return render (request, 'configuracion/configuracion.html',context)
