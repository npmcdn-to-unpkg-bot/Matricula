from django.db import models

# Create your models here.
class Alumnos(models.Model):
	list_genero=(
		('Masculino','Masculino'),
		('Femenino','Femenino'),
	)
	cedula=models.CharField(max_length=12,default="",unique=True)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=30)
	edad=models.SmallIntegerField(default=0)
	email=models.EmailField(max_length=30,blank=True,null=True)
	genero=models.CharField(max_length=10,choices=list_genero,default="Masculino")

	def __str__(self):
		return self.cedula

class Materia(models.Model):
	nombre=models.CharField(max_length=40)
	codigo=models.CharField(max_length=5,default="",unique=True)
	cupos=models.SmallIntegerField(default=0)
	matriculados=models.SmallIntegerField(default=0)

	def __str__(self):
		return self.codigo

class Registros(models.Model):
	idAlumno=models.CharField(max_length=12)
	idMateria=models.CharField(max_length=5)

	def __str__(self):
		return self.idAlumno