from my_app import db
from todos.models import ToDo


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    todos = db.relationship('ToDo', backref = 'user', cascade = 'all, delete-orphan', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % self.username


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
            }
