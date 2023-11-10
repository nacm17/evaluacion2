from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import mercadeo1


# Create your views here.

def home(request):
    mercadeoListado = mercadeo1.objects.all()
    return render(request,"mercadeog.html", {"Mercadeo":mercadeoListado})

def borrar_mercadeo(request,id):
    mercadeo = mercadeo1.objects.get(id=id)
    mercadeo.delete()

    return redirect('/')

def registrar_mercadeo(request):
    cantidad_registrada = request.POST['cantidad_registradax']
    cantidad_vendida = request.POST['cantidad_vendidax']
    ganancia = request.POST['gananciax']
    empresa_transporte = request.POST['empresa_transportex']
    stock_minimo = request.POST['stock_minimox']
    fecha_compra = request.POST['fecha_comprax']

    mercadeo = mercadeo1.objects.create(cantidad_registrada=cantidad_registrada, cantidad_vendida=cantidad_vendida, ganancia=ganancia, empresa_transporte=empresa_transporte, stock_minimo=stock_minimo, fecha_compra=fecha_compra)
    return redirect('/')