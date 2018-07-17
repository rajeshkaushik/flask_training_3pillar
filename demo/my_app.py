from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#    app.config['BUNDLE_ERRORS'] = True

    api = Api(app)
    from users.v1.views import UserListApi, UserApi
    api.add_resource(UserListApi, '/api/v1.0/users')
    api.add_resource(UserApi, '/api/v1.0/users/<int:user_id>')
    db.init_app(app)
    return app
