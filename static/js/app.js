var app = angular.module("twitWriteApp", []);

app.config(['$interpolateProvider', function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
}]);

app.config(function ($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.controller('DummyController', ['$scope', '$http', function ($scope, $http) {
}]);
app.controller("TweetController", ["$scope", "$http", "$q", function ($scope, $http, $q) {

  console.log("TweetController");
  $scope.title = "";
  $scope.body = "";
  $scope.signature = "";
  $scope.loading = false;

  $scope.$watch("share_url", function () {
    console.log($scope.share_url);
  });

  $scope._download = function(share){
    var deferred = $q.defer();
    if (share){
      html2canvas($("#tweet"), {
        onrendered: function (canvas) {
          return deferred.resolve({"image_data": canvas.toDataURL()});
        }
      });
      return deferred.promise;
    }
    else{
      html2canvas($("#tweet"), {
        onrendered: function (canvas) {
          canvas.toBlob(function(blob) {
            saveAs(blob, "tweet.png");
          });
          // Canvas2Image.saveAsPNG(canvas);
        }
      });
    }
  };

  $scope.download = function () {
    console.log("download")
    $scope._download(false);
  };

  $scope.clear = function(){
    $scope.title = "";
    $scope.body = "";
    $scope.signature = "";
  };

  $scope.share = function(){
    console.log("share");
    $scope.loading = true;
    console.log($scope);
    console.log($scope.loading);
    var result = $scope._download(true);
    result.then(function(data){
      var csrf = $("input[name=csrfmiddlewaretoken]").val();
      var data = {
        csrfmiddlewaretoken: csrf,
        image: data.image_data,
      };
      $http.post($scope.share_url, $.param(data))
      .success(function (data) {
        console.log("success");
        console.log(data);
        if (data.status) {
          window.location = data.success_url;
        }
        else {
          window.location = data.error_url;
        }
        $scope.loading = false;
      })
      .error(function (data) {
        $scope.loading = false;
        console.log("error");
      });
    })
  };
}]);
