from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal, Api
# from flask.ext.sqlalchemy import SQLAlchemy
# import os


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
# app.config.from_objects(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from models import Card_Model
from models import User_Model

@app.route('/')
def index():
    return '/ index'

class Cards(Resource):
    def get(self):
        return Card_Model.Card.get_cards()

api.add_resource(Cards, '/cards')

class Users(Resource):
    def get(self, id):
        # parser.add_argument('id', type=int)
        # args = parser.parse_args()
        # id = args.get('id')
        # /users?id=
        return User_Model.User.get_users() if not id else User_Model.User.get_user(id)
    def post(self):
        return User_Model.User.create_user()
    def put(self):
        return User_Model.User.update_user()
    def delete(self):
        return User_Model.User.delete_user()

api.add_resource(Users, '/users')
api.add_resource(Users, '/<int:id>', endpoint='users')



# @app.route('/cards')
# def cards():
#     return Card.Card_Model.get_cards()

# @app.route('/users')
# def get_users():
#     return User.User_Model.get_users()

# @app.route('/users/id')
# def get_user():
#     return User.User_Model.get_user(1)

# @app.route('/users/create')
# def create_user():
#     return User.User_Model.create_user()

# @app.route('/users/update')
# def update_user():
#     return User.User_Model.update_user()

# @app.route('/users/delete')
# def delete_user():
#     return User.User_Model.delete_user()

if __name__ == "__main__":
    app.run(debug=True)