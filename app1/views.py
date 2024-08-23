from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("BIENVENIDOS A DJANGO")

def nuevo(request):
    return HttpResponse("MENSAJE DESDE LA RUTA 127.0.0.1:8000/NUEVO ")

def welcome(request):
    return render(request,'welcome.html',{
        'nombreAplicacion':'app1'
    })