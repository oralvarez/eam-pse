app.controller('myController', function($scope, $http, ProductoService) {
	var query = ProductoService.query();
	query.$promise.then(function(data){
		console.log(data);
		$scope.productos = data.results;
	});	
});


/*

*/