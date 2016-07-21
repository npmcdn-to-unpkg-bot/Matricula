var app = angular.module("app",["ngResource"]);
//Definir el controlador
app.controller("controlador",function($scope,datos,datos_materias,datos_registro){
	$scope.mensaje ="saludos";
	$scope.lista_alumnos= datos.get();
	$scope.lista_materias= datos_materias.get();
	$scope.lista_registos=datos_registro.get();

	$scope.validar = function(a){
		var dato = $scope.cedula;
		var mensaje="hola";

		for(var i=0 ; i< $scope.lista_alumnos.length; i++){
			if ( angular.equals(dato, $scope.lista_alumnos[i].cedula)) {
				window.location.href="datos.html";
			}
			else{
				mensaje="No se valido la cedula";
			}
		}	
		return mensaje;
	}

});
 //Definir el factori que retorne datos del webservice
 app.factory("datos",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/api/alumno/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])
 
 app.factory("datos_materias",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/api/materia/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])

app.factory("datos_registro",['$resource',function($resource){
 	return $resource('http://127.0.0.1:8000/api/registro/',{},{get:{method:'GET',pararms:{}, isArray:true}});
 	}
 ])