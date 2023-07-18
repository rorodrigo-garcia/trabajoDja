from django.urls import path
from .views import index,verEstudiante

app_name='CORE'
urlpatterns = [
    path('',index,name="index"),
    path('',verEstudiante,name="estudiantes")
]
