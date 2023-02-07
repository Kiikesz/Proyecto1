from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="Start"),
    # path('agregar_profes/', agregar_profesor),
    path('ver_estudiantes/', Estudiantes, name="ver estudiantes"),
    path('ver_entregables/', Entregables, name="ver entregables"),
    path('ver_cursos/', Cursos, name="ver cursos"),
    # path('agregar_curso/', agregar_curso),
    # path('agregar_entregable/', agregar_entregable),
    # path('agregar_estudiante/', agregar_estudiante),
    path('ver_profesores/', Profesores, name="ver porfesores"),
    # path('agregar_familiar/', agregar_familiar),
    path('crear_estudiante/', crear_estudiante , name='crear estudiante'),
    path('crear_curso/', crear_curso, name='crear curso'),
    path('crear_profesor/', crear_profesor, name='crear profesor'),
    path('crear_entregables/', crear_entregable, name='crear entregable'),
    path('resultado/', busquedacursos, name='resultado busqueda'),
    path('resultado_entregable/', resultado_entregable , name='resultado entregable'),
    path('resultado_estudiante/', resultado_estudiante  , name='resultado estudiante'),
    path('resultado_profesor/', resultado_profesor, name='resultado profesor'),
]
    