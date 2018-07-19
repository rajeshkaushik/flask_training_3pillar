from my_app import db, create_app

app = create_app('development')

with app.app_context():
    db.create_all()
