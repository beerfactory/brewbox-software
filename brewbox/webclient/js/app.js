/**
 * Created by Vincent on 28/10/2014.
 */
'use strict';

/* App Module */

var brewBoxApp = angular.module('brewBoxApp', [
    'ngRoute',
    'brewBoxControllers',
    'brewBoxServices'
]);

brewBoxApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'templates/index.html',
                controller: 'IndexController'
            }).
            when('/todos', {
                templateUrl: 'templates/todos.html',
                controller: 'TodosController'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);
