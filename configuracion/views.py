from django.shortcuts import redirect, render
from configuracion.forms import ServicioOfrecidoForm
from configuracion.models import ServicioOfrecido


# Create your views here.
def servicioOfrecido(request):
    titulo='Servicio Ofrecido'
    servicios=ServicioOfrecido.objects.all()
    context={
        'titulo':titulo,
        'servicios':servicios,
    }
    return render (request, 'configuracion/servicioOfrecido.html',context)

def servicioOfrecido_crear(request):
    titulo='Servicio Ofrecido / crear'
    if request.method=="POST":
        form=ServicioOfrecidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicioOfrecido')
        else:
            print("Error")
    else:
        form=ServicioOfrecidoForm()

    context={
        'titulo':titulo,
        'form':form,
    }
    return render (request, 'configuracion/servicioOfrecido-crear.html',context)
