import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED True
    SECRET_KEY = 'this_should_really_be_changed'
    SQLALCHEMY_DATABASE_URI