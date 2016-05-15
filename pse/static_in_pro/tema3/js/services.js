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

app.factory('LocalizacionService', function($resource) {
  return $resource('/api/localizacion/:id', {id: '@id'}, 
	{ query	: {method: 'GET', isArray: false}, 
	  post	: {method: 'POST'},
      update: {method: 'PUT'},
      remove: {method: 'DELETE'}
	}); // Note the full endpoint address
});
