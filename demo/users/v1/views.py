from flask_restful import Resource, reqparse, abort, fields, marshal_with, marshal

from users.models import User
from users import auth
from my_app import db


class UserListApi(Resource):
    decorators = [auth.login_required]

    def get(self):
        users = User.query.all() 
        return {'users': [user.to_dict() for user in users]}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username is required')
        parser.add_argument('email', type=str, required=True)

        user = parser.parse_args()

        user = User(**user)
        db.session.add(user)
        db.session.commit()
        return {'user': user.to_dict()}

class UserApi(Resource):

    user_resource_fields = {
        'username': fields.String,
        'email':  fields.String
    }

    @marshal_with(user_resource_fields)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first() 
        if not user:
            abort(404, message="User {} doesn't exist".format(user_id))
        return user


    #@marshal_with(user_resource_fields)
    def put(self, user_id):
        user = User.query.filter_by(id=user_id).first() 
        if not user:
            abort(404, message="User {} doesn't exist".format(user_id))
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help='username is required')
        parser.add_argument('email', type=str, required=True)

        args = parser.parse_args()
        user.username = args['username']
        user.email =  args['email']
        db.session.add(user)
        db.session.commit()
        #return user
        return marshal(user, self.user_resource_fields), 200


    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first() 
        if not user:
            abort(404, message="User {} doesn't exist".format(user_id))
        db.session.delete(user)
        db.session.commit()
        return '', 204
