from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, FileResponse
from django.urls import reverse
from .models import datosUsuario, publicacion, comentario
from django.contrib.auth.models import User
import json

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Create your views here.
def ingresoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usrObj = authenticate(request,username=nombreUsuario, password=contraUsuario)
        if usrObj is not None:
            login(request,usrObj)
            return HttpResponseRedirect(reverse('app4:informacionUsuario'))
        else:
            return HttpResponseRedirect(reverse('app4:ingresoUsuario'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='/')
def informacionUsuario(request):
    allPubs = publicacion.objects.all().order_by('-id')
    return render(request,'informacionUsuario.html',{
        'allPubs':allPubs
    })

@login_required(login_url='/')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('app4:ingresoUsuario'))

def ejemploJs(request):
    return render(request,'ejemploJs.html')

def crearPublicacion(request):
    if request.method == 'POST':
        tituloPub = request.POST.get('tituloPub')
        descripcionPub = request.POST.get('descripcionPub')
        publicacion.objects.create(
            titulo=tituloPub,
            descripcion=descripcionPub,
            autorPublicacion=request.user
        )
        return HttpResponseRedirect(reverse('app4:informacionUsuario'))
    
def devolverDatos(request):
    return JsonResponse({
        'nombre':'Alexander',
        'edad':'25',
        'colegio':'AlmiranteMiguelGrau-Marcona'
    })

def devolverUsuario(request):
    idUsuario = request.GET.get('idUsuario')
    objUsr = User.objects.get(id=idUsuario)
    return JsonResponse({
        'nombre':objUsr.first_name,
        'apellido':objUsr.last_name,
        'email':objUsr.email
    })

def devolverPub(request):
    datosComentarios = []
    idPub = request.GET.get('idPub')
    pubObj = publicacion.objects.get(id=idPub)
    comentariosPub = pubObj.comentario_set.all()
    for comentarioInfo in comentariosPub:
        datosComentarios.append([
            str(comentarioInfo.autorComentario.username),
            comentarioInfo.descripcion
        ])
    return JsonResponse({
        'titulo':pubObj.titulo,
        'descripcion':pubObj.descripcion,
        'nombreAutor':pubObj.autorPublicacion.first_name,
        'apellidoAutor':pubObj.autorPublicacion.last_name,
        'datosComentarios':datosComentarios
    })

def eliminarPub(request,idPub):
    pubObj = publicacion.objects.get(id=idPub)
    pubObj.delete()
    return HttpResponseRedirect(reverse('app4:informacionUsuario'))


def publicarComentario(request):
    datosComentario = json.load(request)
    comentarioTexto = datosComentario.get('comentario')
    idPublicacion = datosComentario.get('idPublicacion')
    objPublicacion = publicacion.objects.get(id=idPublicacion)
    comentario.objects.create(
        descripcion=comentarioTexto,
        autorComentario=request.user,
        pubRelacionada=objPublicacion
    )
    return JsonResponse({
        'resp':'ok'
    })

def descargarReporte(request):
    pubsAll = publicacion.objects.all().order_by('id')
    nombreArchivo = 'reporte.pdf'
    reportePub = canvas.Canvas(nombreArchivo,A4)

    reportePub.drawImage('./app4/static/img/logoApp.png',20,700, width=140,height=80)
    reportePub.drawImage('./app4/static/img/logoPUCP.png',430,700, width=140,height=80)

    reportePub.setFont('Helvetica-Bold',25)
    reportePub.drawCentredString(297.5,730,'REPORTE DE PUBS')

    reportePub.setFont('Helvetica-Bold',12)
    reportePub.drawString(40,620,'Username')
    reportePub.drawString(40,605,'Nombre')
    reportePub.drawString(40,590,'Apellido')
    reportePub.drawString(40,575,'Email')

    reportePub.drawString(155,620,':')
    reportePub.drawString(155,605,':')
    reportePub.drawString(155,590,':')
    reportePub.drawString(155,575,':')

    reportePub.setFont('Helvetica',12)
    reportePub.drawString(160,620,f"{request.user.username}")
    reportePub.drawString(160,605,f"{request.user.first_name}")
    reportePub.drawString(160,590,f"{request.user.last_name}")
    reportePub.drawString(160,575,f"{request.user.email}")

    reportePub.setFont('Helvetica-Bold',12)
    reportePub.drawString(300,620,'Profesion')
    reportePub.drawString(300,605,'Nro Celular')

    reportePub.drawString(425,620,':')
    reportePub.drawString(425,605,':')

    reportePub.setFont('Helvetica',12)
    reportePub.drawString(430,620,f"{request.user.datosusuario.profesion}")
    reportePub.drawString(430,605,f"{request.user.datosusuario.nroCelular}")

    lista_x = [40,550]
    lista_y = [500,540]
    reportePub.setStrokeColorRGB(1,0,0)

    for pubInfo in pubsAll:
        reportePub.grid(lista_x,lista_y)
        reportePub.setFont('Helvetica',12)
        reportePub.drawString(lista_x[0] + 20, lista_y[1] - 15, f"{pubInfo.titulo}")
        reportePub.drawString(lista_x[0] + 220, lista_y[1] - 15, f"{pubInfo.autorPublicacion.username}")
        reportePub.drawString(lista_x[0] + 20, lista_y[1] - 35, f"{pubInfo.descripcion}")
        lista_y[0] = lista_y[0] - 60
        lista_y[1] = lista_y[1] - 60
    reportePub.save()

    reportePubFile = open(nombreArchivo,'rb')
    return FileResponse(reportePubFile,as_attachment=True)

def reactjs(request):
    return render(request,'react.html')