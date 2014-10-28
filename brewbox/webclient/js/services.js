/**
 * Created by Vincent on 28/10/2014.
 */
'use strict';

/* Services */

var brewBoxServices = angular.module('brewBoxServices', ['ngResource']);

brewBoxServices.factory('Todos', ['$resource',
    function($resource){
        return $resource('http://localhost:5001/api/todos', {}, {
            query: {method:'GET', /*params:{phoneId:'phones'}, */ isArray:true}
        });
    }]);
