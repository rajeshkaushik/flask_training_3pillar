from flask_testing import TestCase

#import sys
#sys.path.append('/Users/rajesh.kaushik/projects/flask_tutorial/flask_training_3pillar/demo')
from my_app import create_app, db


class MyTestCase(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
