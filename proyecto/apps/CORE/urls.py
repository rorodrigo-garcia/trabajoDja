from django.urls import path
from .views import index,crearEstudiante

app_name='CORE'
urlpatterns = [
    path('',index,name="index"),
    path('crearEstudiante',crearEstudiante,name="crearEstudiante")
]
