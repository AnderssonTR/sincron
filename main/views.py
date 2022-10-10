from django.shortcuts import render
from django.views.defaults import page_not_found

def inicio(request):
    titulo='Dashboard'
    context={
        'titulo':titulo,
    }
    return render(request,'index.html',context)

def inicioSesion(request):
    titulo='Inicio Sesion'
    context={
        'titulo':titulo,
    }
    return render(request,'login.html',context)

def error_404(request,exception):
    return page_not_found(request,'404.html')