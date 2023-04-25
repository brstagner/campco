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
        User.register(username="test", email="test@email.com", password="password")
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        User.query.delete()
        Campaign.query.delete()

    # Test create
    def test_1_create_get(self):
        """Load create page"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            resp = client.get("/campaign/create")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Create Campaign</h1>", html)

    def test_2_create_post(self):
        """Create a new campaign"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            resp = client.post(
                "/campaign/create",
                follow_redirects=True,
                data={
                    "name": "testcampaign",
                    "password": "password",
                    "repassword": "password",
                    "description": "campaign description",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>testcampaign</h1>", html)

    # Test edit
    def test_3_edit_get(self):
        """Load edit page"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            campaign_id = Campaign.query.first().campaign_id
            resp = client.get(f"/campaign/{campaign_id}/edit", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Edit testcampaign</h1>", html)

    def test_4_edit_post(self):
        """Edit user"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            campaign_id = Campaign.query.first().campaign_id
            resp = client.post(
                f"/campaign/{campaign_id}/edit",
                follow_redirects=True,
                data={
                    "name": "TestCampaign",
                    "description": "Campaign Description",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>TestCampaign</h1>", html)
