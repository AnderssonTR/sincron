from django.shortcuts import render

def inicio(request):
    titulo='Inicio'
    context={
        'titulo':titulo,
    }
    return render(request,'index.html',context)