var app = angular.module('MyApp', []);
app.controller('MyController', function($scope,$http) {
    $scope.ResultsTable=false;
    $scope.MainTable_Progress_Bar=false;

    $scope.search = function() {
      var input = $scope.search_bar;
      console.log(input);
      if($scope.checked1)
        console.log($scope.slider1);

      if($scope.checked2)
        console.log($scope.slider2);

      if($scope.checked3)
        console.log($scope.slider3);

      if($scope.checked4)
        console.log($scope.slider4);

      if($scope.checked5)
        console.log($scope.slider5);

      if($scope.checked6)
        console.log($scope.slider6);

      $scope.resultsArray = [
    {name:'Google', desc:'The best company on the planet once built on ripped off Apple.',age:25, gender:'boy'},
    {name:'Facebook', desc:'The best company on the planet once built on ripped off Apple.',age:30, gender:'girl'},
    {name:'Microsoft', desc:'The best company on the planet once built on ripped off Apple.' , age:28, gender:'girl'},
    {name:'Amazon', desc:'The best company on the planet once built on ripped off Apple.' , age:15, gender:'girl'},
    {name:'Cisco', desc:'The best company on the planet once built on ripped off Apple.' , age:28, gender:'girl'},
    {name:'Yahoo', desc:'The best company on the planet once built on ripped off Apple.' , age:95, gender:'boy'},
    {name:'Visa', desc:'The best company on the planet once built on ripped off Apple.' , age:50, gender:'boy'},
    {name:'VMWare', desc:'The best company on the planet once built on ripped off Apple.' , age:27, gender:'girl'},
    {name:'Ebay', desc:'The best company on the planet once built on ripped off Apple.' , age:40, gender:'boy'},
    {name:'Adobe', desc:'The best company on the planet once built on ripped off Apple.' , age:60, gender:'girl'}
  ];

        //activating results table and progress bar
        $scope.ResultsTable=true;
        //$scope.MainTable_Progress_Bar=true;

    }//End of function search




});
