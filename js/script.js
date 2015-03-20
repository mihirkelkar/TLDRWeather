angular.module( "tldr", ['ngAutocomplete'])
  .controller("tldrCtrl",function ($scope, $http) {
    $scope.resultserver = "";
    $scope.resultimage= "";
    $scope.resultsentence="";
    $scope.submit = function() {
        //console.log($scope.resultserver);
        $http.get("weather/" + $scope.resultserver)
        .success(function(response) {
            console.log(response);
            $scope.resultimage = response.image;
            $scope.resultsentence = response.sentence;
            
        });
    }; 
    
    
});
