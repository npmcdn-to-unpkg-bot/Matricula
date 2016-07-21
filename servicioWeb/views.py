from registro.models  import Materia,Registros,Alumnos
from rest_framework import viewsets
from .serializable import MateriasSerializable,AlumnosSerializable, RegistrosSerializable

class MateriaViewSet(viewsets.ModelViewSet):
	queryset=Materia.objects.filter(cupos__lte=29)
	serializer_class=MateriasSerializable

class AlumnosViewSet(viewsets.ModelViewSet):
	queryset=Alumnos.objects.all().order_by("nombre")
	serializer_class=AlumnosSerializable

class RegistrosViewSet(viewsets.ModelViewSet):
	queryset=Registros.objects.all()
	serializer_class=RegistrosSerializable
