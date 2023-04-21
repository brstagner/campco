from unittest import TestCase
from app import app

class App(TestCase):
    def test_login(self):
        with app.test_client() as client:
            resp = client.get('/login')
            # html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # self.assertIn('<h1>Login</h1>', html)