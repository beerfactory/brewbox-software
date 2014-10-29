/**
 * Created by Vincent on 28/10/2014.
 */

'use strict';

/* Controllers */

var brewBoxControllers = angular.module('brewBoxControllers', []);

brewBoxControllers.controller('IndexController', ['$scope', function($scope)
{
    $scope.name = "Test Angular";
}]);

brewBoxControllers.controller('TodosController', ['$scope', 'Todos', function($scope, Todos)
{
    $scope.name = "Test Angular TODOS";
    $scope.todos = Todos.get({}, function() {});
}]);

/*
phonecatControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', 'Phone',
    function($scope, $routeParams, Phone) {
        $scope.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
            $scope.mainImageUrl = phone.images[0];
        });

        $scope.setImage = function(imageUrl) {
            $scope.mainImageUrl = imageUrl;
        }
    }]);
*/