from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    url(r'^$', 'registro.views.listar'),
    url(r'^crearAlumno/$', 'registro.views.crearAlum'),
    url(r'^crearMateria/$', 'registro.views.crearMateria'),
    url(r'^modificarAlumno/$', 'registro.views.modificarAlumno'),
    url(r'^modificarMateria/$', 'registro.views.modificarMateria'),
    url(r'^eliminarAlumno/$', 'registro.views.eliminarAlumno'),
    url(r'^eliminarMateria/$', 'registro.views.eliminarMateria'),
	url(r'^eliminarAlum/$', 'registro.views.eliminarAlum'),
	url(r'^eliminarMat/$', 'registro.views.eliminarMat'),
    url(r'^matricular/$', 'registro.views.matricular'),
    url(r'^registrar/$', 'registro.views.registrar'),
]