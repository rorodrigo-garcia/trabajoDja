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

def crearProfesor(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form =ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfesorForm()
    return render(request,"CORE/crearProfesor.html",{"form":form})

def crearCurso(request: HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    return render(request,"CORE/crearCurso.html" ,{"form":form})