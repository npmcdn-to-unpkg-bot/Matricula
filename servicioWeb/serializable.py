from registro.models  import Materia,Registros,Alumnos
from rest_framework import serializers

class AlumnosSerializable(serializers.ModelSerializer):
	class Meta:
		model=Alumnos
		fields=['cedula','nombre','apellido']

class MateriasSerializable(serializers.ModelSerializer):
	class Meta:
		model=Materia
		fields=['nombre','codigo','cupos','matriculados']

class RegistrosSerializable(serializers.ModelSerializer):
	class Meta:
		model=Registros
		fields=['idAlumno','idMateria']
