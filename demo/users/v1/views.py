from flask import jsonify, request, abort

from users.models import User
from my_app import app, db

@app.route('/api/v1.0/users', methods=['GET'])
def get_users():
    users = User.query.all() 
    return jsonify({'users': [user.to_dict() for user in users]})


@app.route('/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first() 
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app.route('/api/v1.0/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    if not request.json or not 'email' in request.json:
        abort(400)
    user = {
        'username': request.json['username'],
        'email': request.json.get('email'),
    }
    user = User(**user)
    db.session.add(user)
    db.session.commit()
    return jsonify({'user': user.to_dict()}), 201

@app.route('/api/v1.0/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first() 
    if not user:
        abort(404)
    if not request.json or not 'username' in request.json:
        abort(400)
    if not request.json or not 'email' in request.json:
        abort(400)
    user.username = request.json['username']
    user.email =  request.json.get('email')
    db.session.add(user)
    db.session.commit()
    return jsonify({'user': user.to_dict()}), 200


@app.route('/api/v1.0/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first() 
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})
