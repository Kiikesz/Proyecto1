from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from django.template import Template, Context
from AppCoder.forms import *

# Create your views here.


###Viculos HTML###
def inicio(request):

    return render(request,"AppCoder/inicio.html")

def Estudiantes(request):

    return render(request,"AppCoder/ver_estudiantes.html")

def Profesores(request):

    return render(request,"AppCoder/ver_profes.html")

def Entregables(request):

    return render(request,"AppCoder/ver_entregables.html")

def Cursos(request):

    return render(request,"AppCoder/ver_cursos.html")


# ###Funciones de agregación ###

# def agregar_curso(request):
    
#     curso1 = Curso(nombre="x", camada="x", comision="x")
#     curso1.save()
#     HttpResponse("hemos agregado un curso a la BD.")

# def agregar_entregable(request):
    
#     entregable1 = Entregable(nombre="x", fecha="yyyy/mm/dd", entregado="x@x.com")
#     entregable1.save()
#     HttpResponse("hemos agregado un profesor a la BD.")


# def agregar_estudiante(request):
    
#     estudiante1 = Estudiante(nombre="x", apellido="x", email="x@x.com")
#     estudiante1.save()
#     HttpResponse("hemos agregado un estudiante a la BD.")
    
# def agregar_profesor(request):
    
#     profe1 = Profesor(nombre="x", apellido="x", email="x@x.com", profesion= "x", edad=1)
#     profe1.save()
#     HttpResponse("hemos agregado un profesor a la BD.")

# def agregar_familiar(request):
    
#     familiar1 = Familiar(parentesco="x", nombre="x", edad=1, fecha= "yyyy/mm/dd")
#     familiar1.save()
#     HttpResponse("hemos agregado un profesor a la BD.")



### Creación #####

def crear_estudiante(request):
    if request.method == 'POST':
        miformulario4 =  formularioestudiante(request.POST)
        if miformulario4.is_valid():
            infodict = miformulario4.cleaned_data
            estu1= Estudiante(nombre=infodict["nombre"], apellido = infodict["apellido"], email = infodict["email"])
            estu1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario4 = formularioestudiante()
    return render(request,"AppCoder/crear_estudiante.html", {"formulariestudiante":miformulario4})



def crear_curso(request):
    if request.method == 'POST':
        miformulario =  Cursoformulario(request.POST)
        if miformulario.is_valid():
            infodict = miformulario.cleaned_data
            curso1= Curso(nombre=infodict["nombre"], camada = infodict["camada"], comision= infodict["comision"])
            curso1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario = Cursoformulario()
    return render(request,"AppCoder/crear_curso.html", {"formulariocurso":miformulario})


def crear_profesor(request):
    if request.method == 'POST':
        miformulario1 =  ProfesorFormulario(request.POST)
        if miformulario1.is_valid():
            infodict = miformulario1.cleaned_data
            profe1= Profesor(nombre=infodict["nombre"], apellido = infodict["apellido"], email= infodict["email"], profesion= infodict["profesion"], edad= infodict["edad"],)
            profe1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario1 = ProfesorFormulario()
    return render(request,"AppCoder/crear_profesor.html", {"formularioprofesor":miformulario1})


def crear_entregable(request):
    if request.method == 'POST':
        miformulario3 =  EntregableFormulario(request.POST)
        if miformulario3.is_valid():
            infodict = miformulario3.cleaned_data
            entre1= Entregable(nombre=infodict["nombre"], fecha = infodict["fecha"], entregado = infodict["entregado"])
            entre1.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miformulario3 = EntregableFormulario()
    return render(request,"AppCoder/crear_entregable.html", {"formularioentregable":miformulario3})



### Busquedas ###

def busquedacursos(request):

    if request.method =="GET":
        busquedacomision = request.GET["comision"]
        comisionresultado = Curso.objects.filter(comision__icontains=busquedacomision)
        return render(request,"AppCoder/resultado.html", {"comision":busquedacomision, "resultados":comisionresultado})
    
    return render(request, "AppCoder/ver_curso.html")

def resultado_entregable(request):

    if request.method =="GET":
        busquedaentregable = request.GET["nombre"]
        entregableresultado = Entregable.objects.filter(nombre__icontains=busquedaentregable)
        return render(request,"AppCoder/resultado_entregable.html", {"nombre":busquedaentregable, "resultados":entregableresultado})
    
    return render(request, "AppCoder/ver_entregables.html")

def resultado_estudiante(request):

    if request.method =="GET":
        busquedaestudiante = request.GET["email"]
        estudianteresultado = Estudiante.objects.filter(email__icontains=busquedaestudiante)
        return render(request,"AppCoder/resultado_estudiante.html", {"email":busquedaestudiante, "resultados":estudianteresultado})
    
    return render(request, "AppCoder/ver_estudiantes.html")

def resultado_profesor(request):

    if request.method =="GET":
        busquedaprofesor = request.GET["email"]
        proferesultado = Profesor.objects.filter(email__icontains=busquedaprofesor)
        return render(request,"AppCoder/resultado_profesor.html", {"email":busquedaprofesor, "resultados":proferesultado})
    
    return render(request, "AppCoder/ver_profesor.html")