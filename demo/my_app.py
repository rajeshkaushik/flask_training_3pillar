from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    api = Api(app)

    from users.v1.views import UserListApi, UserApi
    api.add_resource(UserListApi, '/api/v1.0/users')
    api.add_resource(UserApi, '/api/v1.0/users/<int:user_id>')
    db.init_app(app)
    return app
