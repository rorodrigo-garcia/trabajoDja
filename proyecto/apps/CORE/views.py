from django.shortcuts import render,redirect
from .models import Estudiante,Profesor,Curso

def index(request):
    return render(request,'CORE/index.html')

def verEstudiante(request):
    estudiantesRegistrados = Estudiante.objects.all()
    contexto = {"estudiantes" : estudiantesRegistrados}
    return  render ( request,"CORE/index.html",contexto)
