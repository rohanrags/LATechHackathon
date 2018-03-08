var app = angular.module('MyApp1', []);
app.controller('MyController1', function($scope,$http) {
    $scope.bar_graph=false;
    $scope.extraDiv=true;

    $scope.upload = function() {
      $scope.extraDiv=false;
      $scope.bar_graph=true;

      var req = {
         method: 'POST',
         url: 'http://192.168.1.16:5000/evaluate',
         headers: {
           'Content-Type': 'application/json'
         },
         data: {
            "vol":"2","papers":"3","work":"1","c":"2","html":"2","css":"1","bootstrap":"1","python":"9","ml":"8","nlp":"10","mvc":"7","ang":"7","java":"6","tablaeu":"3","R":"2","stats":"1","linux":"3","windows":"4","multithread":"1"
          }
      }

      $http(req).then(function successCallback(response) {
            $scope.status = response.status;
            //$scope.data = response.data;
            $scope.resultsArray = response.data;
            console.log($scope.status);
            console.log($scope.resultsArray.jsonobj.Back);

            var data = {
              labels: ["Web Development", "Data Science", "Data Analytics", "Back End Development", "Systems Development"],
              datasets: [{
                label: "Results against best employees in the Industry",
                backgroundColor: "rgba(255,99,132,0.2)",
                borderColor: "rgba(255,99,132,1)",
                borderWidth: 2,
                hoverBackgroundColor: "rgba(255,99,132,0.4)",
                hoverBorderColor: "rgba(255,99,132,1)",
                data: [$scope.resultsArray.jsonobj.Front, $scope.resultsArray.jsonobj.DataScience, $scope.resultsArray.jsonobj.DataAnalytics,$scope.resultsArray.jsonobj.Back, $scope.resultsArray.jsonobj.Systems],
              }]
            };

            var options = {
              maintainAspectRatio: false,
              scales: {
                yAxes: [{
                  stacked: true,
                  gridLines: {
                    display: true,
                    color: "rgba(255,99,132,0.2)"
                  }
                }],
                xAxes: [{
                  gridLines: {
                    display: false
                  }
                }]
              }
            };

            Chart.Bar('chart', {
              options: options,
              data: data
            });


          }, function errorCallback(response) {
            $scope.status = response.status;
            $scope.data = response.data;
            console.log($scope.status);
            console.log($scope.data);
      });
    }
});
