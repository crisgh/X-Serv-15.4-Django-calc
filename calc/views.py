from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def sumar(request, num1, suma, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse('La suma es ' + str(resultado))

def restar(request, num1, resta, num2):
    resultado = int(num1) - int(num2)
    return HttpResponse('La resta es ' + str(resultado))

def multiplicar(request, num1, mult, num2):
    resultado = int(num1) * int(num2)
    return HttpResponse('El producto es ' + str(resultado))

def division(request, num1, div, num2):
    try:
        resultado = int(num1) / int(num2)
        return HttpResponse('El cociente es ' + str(resultado))
    except ZeroDivisionError:
        return HttpResponse('No se puede dividir entre 0')

def 404(request):
    return HttpResponseNotFound('Error 404 :Recursos introducidos invalidos')
