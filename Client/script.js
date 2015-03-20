angular.module( "tldr", ['ngAutocomplete'])
  .controller("tldrCtrl",function ($scope, $http) {
    $scope.resultserver = '';
    $scope.resultimage= "";
    $scope.resultsentence="";

    $http.get("http://tldr-weather.herokuapp.com/weather/" + $scope.resultserver)
    .success(function(response) {
    	$scope.resultimage = response.image;
    	$scope.resultsentence = response.sentence;
    });
});