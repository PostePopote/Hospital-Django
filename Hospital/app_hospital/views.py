from django.http import HttpResponse


from django.shortcuts import render, HttpResponseRedirect


def saludo(request):
    return HttpResponse('Hola Mundo')

def index(request):
    return render(request, 'app_hospital/index.html')

def pacientes(request):
    return render(request, 'app_hospital/pacientes.html')
def medicos(request):
    return render(request, 'app_hospital/medicos.html')
def tratamientos(request):
    return render(request, 'app_hospital/tratamientos.html')