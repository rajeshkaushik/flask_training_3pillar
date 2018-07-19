from tests.conftest import MyTestCase
from my_app import db
from users.models import User
import base64

class TestUserListApi(MyTestCase):


    def setUp(self):
        super().setUp()
        user = User(**{'username': 'u1', 'email':'test1@gmail.com'})
        db.session.add(user)
        db.session.commit()

    def test_valid_response(self):
        resp = self.client.get('/api/v1.0/users', headers={"Authorization": "Basic " + base64.b64encode(b"rajesh:kaushik").decode('utf-8')})
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(resp.json.get('users')))

