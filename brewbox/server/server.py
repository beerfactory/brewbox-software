# Copyright (C) 2014  Nicolas Jouanin and others
#
# This file is part of brewbox.
#
# Brewbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Brewbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

# You should have received a copy of the GNU General Public License
# along with Brewbox.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify, json
from flask.ext.restful import Resource, Api, reqparse

#Configuration
DEBUG = True
SERVER_NAME = "localhost:5001"

#Create application
app = Flask("BrewBox")
app.config.from_object(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=str)
parser.add_argument('task', type=str)

#Some work
@app.route('/')
def rootServer():
    abort(404)

'''
@app.route('/api')
def documentation():
    return auto.html()
'''

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'finish to choice tools'},
    'todo3': {'task': 'have time to work...'},
    }

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, "Todo {} doesn't exist".format(todo_id))

# Todo
#   show a single todo item and lets you delete them
# Access-Control-Allow-Origin temporaire : je vais me coucher :)

class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id], {'Access-Control-Allow-Origin': '*'}

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204, {'Access-Control-Allow-Origin': '*'}

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201, {'Access-Control-Allow-Origin': '*'}


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS, 200, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201, {'Access-Control-Allow-Origin': '*'}

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/api/todos')
api.add_resource(Todo, '/api/todo/<string:todo_id>')


if __name__ == '__main__':
    app.run()
