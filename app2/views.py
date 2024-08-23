from django.shortcuts import render

# Create your views here.

def inicio(request):
    lista_estudiantes = [
        "JAVIER HILARIO",
        "WILDER CARTAGENA",
        "MARTIN LEYVA",
        "DIEGO QUIROZ",
        "JOSE BALBUENA",
        "DAFFER ESCOBAR"
    ]
    rolUsuario = "ADMIN"
    return render(request,'WelcomeApp2.html',{
        "estudiantes":lista_estudiantes,
        "rolUsuario":rolUsuario
    })