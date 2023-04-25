import os
from dotenv import load_dotenv
from unittest import TestCase
from models.user import User
from models.campaign import Campaign
from models.player import Player

load_dotenv()

# Switch to test database before importing app
os.environ["DATABASE_URL"] = os.environ["TEST_DATABASE_URL"]
# Disable CSRF for testing
os.environ["WTF_CSRF_ENABLED"] = "False"

from app import app


class UserTests(TestCase):
    @classmethod
    def setUpClass(cls):
        User.query.delete()
        Campaign.query.delete()
        Player.query.delete()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        User.query.delete()

    # Test register
    def test_1_register_get(self):
        """Load registration page"""
        with app.test_client() as client:
            resp = client.get("/register")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Register a User</h1>", html)

    def test_2_register_post(self):
        """Create a new user"""
        with app.test_client() as client:
            resp = client.post(
                "/register",
                follow_redirects=True,
                data={
                    "username": "test",
                    "email": "test@email.com",
                    "password": "password",
                    "confirm": "password",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>test</h2>", html)

    def test_3_duplicate_register(self):
        """Fail to create a new user with duplicate username/password"""
        with app.test_client() as client:
            self.client = app.test_client()

            resp = client.post(
                "/register",
                follow_redirects=True,
                data={
                    "username": "test",
                    "email": "test@email.com",
                    "password": "password",
                    "confirm": "password",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Email already in use", html)
            self.assertIn("Username already in use, choose a different username", html)

    # Test login/logout
    def test_4_logout(self):
        """Log out"""
        with app.test_client() as client:
            resp = client.get("/logout", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>User Login</h1>", html)

    def test_5_login_get(self):
        """Load login page"""
        with app.test_client() as client:
            resp = client.get("/login")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>User Login</h1>", html)

    def test_6_login_post(self):
        """Login user"""
        with app.test_client() as client:
            resp = client.post(
                "/login",
                follow_redirects=True,
                data={
                    "username": "test",
                    "password": "password",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h4>Email:</h4>", html)

    # Test edit
    def test_7_edit_get(self):
        """Load edit page"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            resp = client.get("/user/edit")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Edit Details for test</h1>", html)

    def test_8_edit_post(self):
        """Edit user"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            resp = client.post(
                "/user/edit",
                follow_redirects=True,
                data={
                    "new_username": "test1",
                    "new_email": "test1@email.com",
                    "current_password": "password",
                    "new_password": "pass",
                    "confirm": "pass",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>test1</h2>", html)
