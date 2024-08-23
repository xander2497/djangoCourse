from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import departamento, persona

# Create your views here.
def directorio(request):
    listaDepartamentos = departamento.objects.all().order_by('id')
    listaPersonas = persona.objects.all()
    return render(request,'directorio.html',{
        'listaDepartamentos':listaDepartamentos,
        'listaPersonas':listaPersonas
    })

def nuevoRegistro(request):
    listaDepartamentos = departamento.objects.all().order_by('id')
    if request.method == 'POST':
        nombreRegistro = request.POST.get('nombreRegistro')
        apellidoRegistro = request.POST.get('apellidoRegistro')
        numeroRegistro = request.POST.get('numeroRegistro')
        emailRegistro = request.POST.get('emailRegistro')
        descripcionRegistro = request.POST.get('descripcionRegistro')
        depaRegistro = request.POST.get('departamentoSeleccionado')
        print(depaRegistro)
        depaRelacionado = departamento.objects.get(id=depaRegistro)
        objPersona = persona.objects.create(
            nombre=nombreRegistro,
            apellido=apellidoRegistro,
            numero=numeroRegistro,
            email=emailRegistro,
            descripcion=descripcionRegistro,
            depaRelacionado=depaRelacionado
        )
        objPersona.save()
        return HttpResponseRedirect(reverse('app3:directorio'))
    return render(request,'nuevoRegistro.html',{
        'listaDepartamentos':listaDepartamentos
    })

def nuevoDepartamento(request):
    listaDepartamentos = departamento.objects.all().order_by('id')
    if request.method == 'POST':
        nombreDepartamento = request.POST.get('nombreDepartamento')
        descripcionDepartamento = request.POST.get('descripcionDepartamento')
        objDepartamento = departamento.objects.create(
            nombreDepartamento=nombreDepartamento,
            descripcionDepartamento=descripcionDepartamento
        )
        objDepartamento.save()
        return HttpResponseRedirect(reverse('app3:directorio'))
    return render(request,'nuevoDepartamento.html',{
        'listaDepartamentos':listaDepartamentos
    })

def vistaDepartamento(request,idDepartamento):
    listaDepartamentos = departamento.objects.all().order_by('id')
    objDeparamento = departamento.objects.get(id=idDepartamento)
    listaUsuarios = objDeparamento.persona_set.all()
    return render(request,'vistaDepartamento.html',{
        'listaDepartamentos':listaDepartamentos,
        'objDepartamento':objDeparamento,
        'listaUsuarios': listaUsuarios
    })

def vistaUsuario(request,idPersona):
    listaDepartamentos = departamento.objects.all().order_by('id')
    objPersona = persona.objects.get(id=idPersona)
    return render(request,'vistaUsuario.html',{
        'listaDepartamentos':listaDepartamentos,
        'objPersona':objPersona,
    })