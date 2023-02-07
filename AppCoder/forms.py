from django import forms

class  Cursoformulario(forms.Form):
     nombre = forms.CharField(max_length=20)
     camada = forms.IntegerField()
     comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    profesion = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class EntregableFormulario(forms.Form):
        nombre = forms.CharField(max_length=20)
        fecha = forms.DateField()
        entregado = forms.BooleanField()

class formularioestudiante(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)