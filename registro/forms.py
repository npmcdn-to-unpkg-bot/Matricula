from django import forms
from .models import Materia,Alumnos

class Form_Materias(forms.ModelForm):
	class Meta:
		model=Materia
		fields=['nombre','codigo','cupos']

class Form_Alumnos(forms.ModelForm):
	class Meta:
		model=Alumnos
		fields=['cedula','nombre','apellido','edad','email','genero']