from django import forms 

from .models import Estudiante,Profesor,Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre","apellido","edad"]

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ["nombre","apellido","especialidad"]

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre","descripcion"]

