from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request, 'app/inicio.html')

def quienes(request):
	return render(request, 'app/quienes.html')

def contacto(request):
	return render(request, 'app/contacto.html')

def preguntas(request):
	return render(request, 'app/preguntas.html')

def evento(request):
	return render(request, 'app/evento.html')

def pre(request):
	return render(request, 'app/pre.html')

