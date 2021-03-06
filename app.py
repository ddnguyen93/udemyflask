import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://guxdfjopmdcdch:5f5f31f2f0b9c618fd67287b1b7c6e50837a02a03aaf1e38983ecb44ab48ffe2@ec2-54-166-120-40.compute-1.amazonaws.com:5432/dcamg5u1ajqci5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"
api = Api(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')

api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

api.add_resource(Store, '/store/<string:name>')

api.add_resource(StoreList, '/stores')

db.init_app(app)

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    
    app.run(port=5000)