angular.module( "tldr", ['ngAutocomplete'])
  .controller("tldrCtrl",function ($scope) {

    $scope.resultserver = '';
    $scope.resultimage= "";
    $scope.resultsentence="";
});