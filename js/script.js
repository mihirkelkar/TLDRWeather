angular.module( "tldr", ['ngAutocomplete'])
  .controller("tldrCtrl",function ($scope, $http) {
    $scope.resultserver = "";
    $scope.resultimage= "";
    $scope.resultsentence="";
    $scope.submit = function() {
        //console.log($scope.resultserver);
        $scope.dataarray = $scope.resultserver.split(",");
        if($scope.dataarray.length <= 2){
          $scope.data = $scope.dataarray.join("");
        } else {
          $scope.data = $scope.dataarray.slice(0, 2).join("");
        }
        $http.get("weather/" + $scope.data)
        .success(function(response) {
            //console.log(response);
            $scope.resultimage = response.image;
            $scope.resultsentence = response.sentence;
            
        });
    }; 
    
    
});
