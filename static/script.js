var app = angular.module('MyApp', []);
app.controller('MyController', function($scope,$http) {
    $scope.ResultsTable=false;
    $scope.extraDiv=true;

    $scope.selectables = [
        { label: 'Technology', value: 'Technology'},
        { label:'Medical', value: 'Medical'},
        { label: 'Finance', value: 'Finance'}
    ];
    //$scope.MainTable_Progress_Bar=false;

    $scope.search = function() {
      $scope.extraDiv=false;

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

      if($scope.checked7)
        console.log($scope.slider7);

      if($scope.checked8)
        console.log($scope.slider8);

      if($scope.selectedItemvalue)
        console.log($scope.selectedItemvalue);

        // $scope.resultsArray = {"WePay": {"Environment": "A+", "CEORating": "A", "Leadership": "A-", "eNPS": "B+", "Sentiment": "B+", "Manager": "B+", "WorkCulture": "B+", "OverallCulture": "B", "ProfessionalDevelopment": "B", "Compensation": "C", "PerkAndBenefits": "B", "Team": "B", "Happiness": "B", "Meetings": "C+", "Diversity": "B", "Gender": "B-", "Retention": "B", "ExecutiveTeam": "C+", "OfficeCulture": "C+", "company_url": "https://www.comparably.com/companies/wepay"
        // }}

        var req = {
           method: 'POST',
           url: 'http://192.168.1.16:5000/search',
           headers: {
             'Content-Type': 'application/json'
           },
           data: {
              "Compensations":$scope.slider1,
              "PerkAndBenefits":$scope.slider2,
              "Retention":$scope.slider3,
              "ProfessionalDevelopment":$scope.slider4,
              "Happiness":$scope.slider5,
              "Environment":$scope.slider6,
              "Leadership":$scope.slider7,
              "WorkCulture":$scope.slider8,
              "domain":$scope.selectedItemvalue
            }
        }

      $http(req).then(function successCallback(response) {
            $scope.status = response.status;
            $scope.data = response.data;
            $scope.resultsArray = response.data;
            console.log($scope.status);
            console.log($scope.data);
          }, function errorCallback(response) {
            $scope.status = response.status;
            $scope.data = response.data;
            console.log($scope.status);
            console.log($scope.data);
      });

      // $.ajax({
      //     url: 'http://192.168.1.16:5000/search',
      //     data: {
      //         "Compensations":"12",
      //         "PerkAndBenefits":"12",
      //         "Retention":"12",
      //         "ProfessionalDevelopment":"12",
      //         "Happiness":"12",
      //         "Environment":"12",
      //         "Leadership":"12",
      //         "WorkCulture":"12",
      //         "domain":"Technology"
      //     },
      //     type: 'POST',
      //     success: function(output) {
      //       console.log(output);
      //       $scope.resultsArray = output;
      //    }
      // });

      // $.ajax('http://192.168.1.16:5000/search',{
      //     'data': {
      //         "Compensations":"12",
      //         "PerkAndBenefits":"12",
      //         "Retention":"12",
      //         "ProfessionalDevelopment":"12",
      //         "Happiness":"12",
      //         "Environment":"12",
      //         "Leadership":"12",
      //         "WorkCulture":"12",
      //         "domain":"Technology"
      //     }, //{action:'x',params:['a','b','c']}
      //     'type': 'POST',
      //     'processData': false,
      //     'contentType': 'application/json',
      //     success: function(output) {
      //       console.log(output);
      //       $scope.resultsArray = output;
      //     }
      // });

      //activating results table and progress bar
      $scope.ResultsTable=true;
      //$scope.MainTable_Progress_Bar=true;

    }//End of function search

});
