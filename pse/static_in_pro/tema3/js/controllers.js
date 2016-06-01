app.controller('myController', function($scope, $http, ProductoService) {
	var query = ProductoService.query();
	query.$promise.then(function(data){
		console.log(data);
		$scope.productos = data.results;
	});	
});

app.controller('logOutController', function($scope, $http, $window) {
	$scope.logout = function() {
		$http({
			url: '/rest-auth/logout/',
			method: "POST",
			//data: postData,
			//headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		}).success(function (data, status, headers, config) {
			console.log(data); // how do pass this to $scope.persons?
			$window.location.href = '/';
		}).error(function (data, status, headers, config) {
			console.log(data);//status;
		});
	}
});

app.controller('myFileUploadController', ['$scope', 'fileUpload', function($scope, fileUpload){
            $scope.uploadFile = function(){
               var file = $scope.myFile;

               console.log('file is ' );
               console.dir(file);

               var uploadUrl = "/fileUpload";
               fileUpload.uploadFileToUrl(file, uploadUrl);
            };
         }]);

/*

*/