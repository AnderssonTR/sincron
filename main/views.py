from django.shortcuts import render

def inicio(request):
    titulo='inicio'
    context={
        'titutlo':titulo,
    }
    return render(request,'index.html',context)