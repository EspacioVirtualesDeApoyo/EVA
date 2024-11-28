from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def educacion(request):
    return render(request, 'educacion.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def sobre_la_app(request):
    return render(request, 'sobre_la_app.html')

def preguntas_frecuentes(request):
    return render(request, 'preguntas_frecuentes.html')

def testimonios(request):
    return render(request, 'testimonios.html')