from django.shortcuts import redirect, render
from configuracion.forms import CategoriasForm, EstadoGesionForm, ServicioOfrecidoForm, SubCategoriasForm
from configuracion.models import Categoria, EstadoGestion, ServicioOfrecido, SubCategoria


# Create your views here.

# Vistas para servicio Ofrecido
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

# Vistas para estado de Gestion

def estadoGestion(request):
    titulo='Estado de Gestión'
    estados=EstadoGestion.objects.all()
    context={
        'titulo':titulo,
        'estados':estados,
    }
    return render (request,'configuracion/estadoGestion.html',context) 

def estadoGestion_crear(request):
    titulo='Estado de Gestión / crear'
    if request.method=="POST":
        form=EstadoGesionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estadoGestion')
        else:
            print("Error")
    else:
        form=EstadoGesionForm()

    context={
        'titulo':titulo,
        'form':form,
    }
    return render (request, 'configuracion/estadoGestion-crear.html',context)


# Vistas para categoria
def categoria(request):
    titulo='Categoria'
    categorias=Categoria.objects.all()
    context={
        'titulo':titulo,
        'categorias':categorias,
    }
    return render (request, 'configuracion/categoria.html',context)

def categoria_crear(request):
    titulo='Categoria / crear'
    if request.method=="POST":
        form=CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria')
        else:
            print("Error")
    else:
        form=CategoriasForm()

    context={
        'titulo':titulo,
        'form':form,
    }
    return render (request, 'configuracion/categoria-crear.html',context)

# Vistas para subCategoria
def subCategoria(request):
    titulo='subCategoria'
    subCategorias=SubCategoria.objects.all()
    context={
        'titulo':titulo,
        'subCategorias':subCategorias,
    }
    return render (request, 'configuracion/subCategoria.html',context)

def subCategoria_crear(request):
    titulo='subCategoria / crear'
    if request.method=="POST":
        form=SubCategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subCategoria')
        else:
            print("Error")
    else:
        form=SubCategoriasForm()

    context={
        'titulo':titulo,
        'form':form,
    }
    return render (request, 'configuracion/subCategoria-crear.html',context)