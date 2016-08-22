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
app.controller('TweetController', ['$scope', '$http', function ($scope, $http) {

  $scope.download = function () {
    html2canvas($("#tweet"), {
      onrendered: function (canvas) {
        canvas.toBlob(function(blob) {
          saveAs(blob, "tweet.png");
        });
        // Canvas2Image.saveAsPNG(canvas);
      }
    });
  }

  $scope.clear = function(){
    $scope.title = "";
    $scope.body = "";
    $scope.signature = "";
  };

  $scope.share = function(){

  };
}]);
