angular.module( "tldr", ['ngAutocomplete'])
  .controller("tldrCtrl",function ($scope, $http) {
    $scope.resultserver = '';
    $scope.resultimage= "";
    $scope.resultsentence="";
    
    console.log($scope.resultserver);

    $http.get("weather/" + $scope.resultserver)
    .success(function(response) {
    	$scope.resultimage = response.image;
    	$scope.resultsentence = response.sentence;
    });
});
