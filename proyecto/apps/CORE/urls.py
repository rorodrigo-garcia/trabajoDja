from django.urls import path
from .views import index,crearEstudiante,crearProfesor,crearCurso

app_name='CORE'
urlpatterns = [
    path('',index,name="index"),
    path('crearEstudiante/',crearEstudiante,name="crearEstudiante"),
    path('crearProfesor/',crearProfesor,name="crearProfesor"),
    path('crearCurso/',crearCurso,name="crearCurso")
]
