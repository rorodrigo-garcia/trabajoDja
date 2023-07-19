from django.shortcuts import render,redirect
from .models import Estudiante,Profesor,Curso
from .forms import EstudianteForm,ProfesorForm,CursoForm
from django.http import HttpRequest,HttpResponse

def index(request):
    estudiantesRegistrados = Estudiante.objects.all()
    profesorRegistrados = Profesor.objects.all()
    cursoRegistrado = Curso.objects.all()
    contexto = {"estudiantes" : estudiantesRegistrados ,"profesores" : profesorRegistrados , "cursos" : cursoRegistrado}
    return  render ( request,"CORE/index.html",contexto)
   

def crearEstudiante(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form =EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EstudianteForm()
    return render(request,"CORE/crearEstudiante.html",{"form":form})
