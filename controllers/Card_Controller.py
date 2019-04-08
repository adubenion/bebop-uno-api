from flask import request
from flask_restful import Resource, reqparse, fields, marshal, Api

from models import Card_Model

parser = reqparse.RequestParser()

class Cards(Resource):
    def get(self):
        return Card_Model.Card.get_cards()