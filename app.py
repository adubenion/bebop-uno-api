from flask import Flask, request
from flask_restful import Resource, reqparse, fields, marshal, Api
# from flask.ext.sqlalchemy import SQLAlchemy
# import os


app = Flask(__name__)
api = Api(app)
# app.config.from_objects(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from controllers import User_Controller
from controllers import Card_Controller

@app.route('/')
def index():
    return '/ index'

api.add_resource(Card_Controller.Cards, '/cards')

api.add_resource(User_Controller.Users, '/users', '/users/', '/users/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)