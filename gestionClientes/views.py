from django.shortcuts import render

# Create your views here.

# Create your views here
def gestionClientes(request):
    titulo='Gestion de clientes'
    context={
        'titulo':titulo,
    }
    return render (request, 'gestionClientes/gestionClientes.html',context)

