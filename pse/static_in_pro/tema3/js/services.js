app.factory('ProductoService', function($resource) {
  return $resource('/api/producto/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});
app.factory('UserService', function($resource) {
  return $resource('/api/users/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('TipoContratoService', function($resource) {
  return $resource('/api/tipocontrato/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('TipoUbicacionService', function($resource) {
  return $resource('/api/tipoubicacion/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('TipoObjetoService', function($resource) {
  return $resource('/api/tipoobjeto/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('TipoProductoService', function($resource) {
  return $resource('/api/tipoproducto/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('MonedaService', function($resource) {
  return $resource('/api/moneda/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('PaisService', function($resource) {
  return $resource('/api/pais/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('DepartamentoService', function($resource) {
  return $resource('/api/departamento/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('CiudadService', function($resource) {
  return $resource('/api/ciudad/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('ClienteService', function($resource) {
  return $resource('/api/cliente/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('DependenciaService', function($resource) {
  return $resource('/api/dependencia/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('AnexoProductoService', function($resource) {
  return $resource('/api/anexoproducto/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false},
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('EstadoProductoService', function($resource) {
  return $resource('/api/estadoproducto/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false},
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('UsuarioDependenciaService', function($resource) {
  return $resource('/api/usuarioDependencia/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false},
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('AccionesEstadoService', function($resource) {
  return $resource('/api/accionesestado/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false},
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('AccionesSourcingService', function($resource) {
  return $resource('/api/accionessourcing/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false},
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

app.factory('DetalleServicioService', function($resource) {
  return $resource('/api/detallesolicitudproducto/:id', {id: '@id'},
	{ query	: {method: 'GET', isArray: false},
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});

/*

    "anexoproducto": "http://127.0.0.1:8000/api/anexoproducto/",
    "estadoproducto": "http://127.0.0.1:8000/api/estadoproducto/",
    "usuarioDependencia": "http://127.0.0.1:8000/api/usuarioDependencia/",
    "accionesestado": "http://127.0.0.1:8000/api/accionesestado/",
    "accionessourcing": "http://127.0.0.1:8000/api/accionessourcing/"
 */
app.service('fileUploadService', ['$http', function ($http) {
            this.uploadFileToUrl = function(file, uploadUrl){
               var fd = new FormData();
               fd.append('file', file);

               $http.post(uploadUrl, fd, {
                  transformRequest: angular.identity,
                  headers: {'Content-Type': undefined}
               })

               .success(function(){
               })

               .error(function(){
               });
            }
         }]);