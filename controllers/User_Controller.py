from flask import request
from flask_restful import Resource, reqparse, fields, marshal, Api

from models import User_Model

parser = reqparse.RequestParser()

class Users(Resource):
    def get(self, id=None):
        return User_Model.User.get_users() if not id else User_Model.User.get_user(id)
    def post(self):
        return User_Model.User.create_user()
    def put(self):
        return User_Model.User.update_user()
    def delete(self):
        return User_Model.User.delete_user()