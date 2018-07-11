from my_app import db


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), default='')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    done = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return '<ToDo %r>' % self.detail


    def to_dict(self):
        return {
            'id': self.id,
            'detail': self.detail,
            'description': self.description,
            'user_id': self.user_id,
            'done': self.done
            }
