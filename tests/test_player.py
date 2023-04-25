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
        user_id = User.query.first().user_id
        Campaign.create(
            user_id=user_id,
            name="testcampaign",
            password="password",
            description="campaign description",
        )
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        User.query.delete()
        Campaign.query.delete()
        Player.query.delete()

    # Test create
    def test_1_create_get(self):
        """Load create page"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            resp = client.get("/player/create")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Player Create</h1>", html)

    def test_2_create_post(self):
        """Create a new player"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                session["user_id"] = User.query.first().user_id
            campaign_id = Campaign.query.first().campaign_id
            resp = client.post(
                "/player/create",
                follow_redirects=True,
                data={
                    "campaign_id": campaign_id,
                    "password": "password",
                    "name": "testplayer",
                },
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Player: testplayer</h2>", html)

    # Test edit

    def test_3_edit_post(self):
        """Edit player"""
        with app.test_client() as client:
            player = Player.query.first()
            with client.session_transaction() as session:
                session["user_id"] = player.user_id
            campaign_id = player.campaign_id
            player_id = player.player_id

            client.post(
                f"/player/{player_id}/edit/demo",
                follow_redirects=True,
                data={
                    "player_level": "2",
                    "player_xp": "2",
                    "race": "{'name':'Elf'}",
                    "subrace": "{'name':'High Elf'}",
                    "job": "Rogue",
                    "subjob": "{'name':'Thief'}",
                    "age": "200",
                    "alignment": "{'name':'Neutral'}",
                    "size": "Medium",
                    "notes": "These are notes",
                },
            )

            client.post(
                f"/player/{player_id}/edit/vitals",
                follow_redirects=True,
                data={
                    "hp": "{'current': 5, 'max': 10}",
                    "hd": "[]",
                    "conditions": "[]",
                },
            )

            client.post(
                f"/player/{player_id}/edit/combat",
                follow_redirects=True,
                data={
                    "attacks": "[]",
                    "ac": "1",
                    "initiative": "1",
                    "speed": "1",
                    "ki": "{'current': 4, 'max': 9}",
                },
            )

            client.post(
                f"/player/{player_id}/edit/spells",
                follow_redirects=True,
                data={
                    "known": "[{'name':'spell', 'desc':'description'}]",
                    "lv0": "[]",
                    "lv1": "[]",
                    "lv2": "[]",
                    "lv3": "[]",
                    "lv4": "[]",
                    "lv5": "[]",
                    "lv6": "[]",
                    "lv7": "[]",
                    "lv8": "[]",
                    "lv9": "[]",
                },
            )

            client.post(
                f"/player/{player_id}/edit/ability",
                follow_redirects=True,
                data={
                    "strength": "1",
                    "constitution": "2",
                    "dexterity": "3",
                    "intelligence": "4",
                    "wisdom": "5",
                    "charisma": "6",
                },
            )

            client.post(
                f"/player/{player_id}/edit/proficiency",
                follow_redirects=True,
                data={
                    "skills": "[{'name':'test skill'}]",
                    "weapons": "[]",
                    "armor": "[]",
                    "tools": "[]",
                    "languages": "[]",
                    "traits": "[]",
                    "features": "[]",
                },
            )

            client.post(
                f"/player/{player_id}/edit/items",
                follow_redirects=True,
                data={
                    "weapons": "[{'name':'test weapon', 'number': 1}]",
                    "armor": "[]",
                    "tools": "[]",
                    "wallet": "[]",
                    "other": "[]",
                    "weight": "{'current':3, 'max':8}",
                },
            )

            client.post(
                f"/player/{player_id}/edit/level",
                follow_redirects=True,
                data={
                    "barbarian": "1",
                    "bard": "0",
                    "cleric": "0",
                    "druid": "0",
                    "fighter": "0",
                    "monk": "0",
                    "paladin": "0",
                    "ranger": "0",
                    "rogue": "0",
                    "sorcerer": "0",
                    "warlock": "0",
                    "wizard": "0",
                },
            )

            resp = client.post(
                f"/player/{player_id}/edit/player",
                follow_redirects=True,
                data={"name": "TestPlayer", "campaign_id": ""},
            )
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Player: TestPlayer</h2>", html)
            self.assertNotIn("Campaign: testcampaign</a></h2>", html)
            self.assertIn("Elf", html)
            self.assertIn("5/10", html)
            self.assertIn("4 / 9", html)
            self.assertIn(
                '<div class="item info" data-desc="description">spell</div>', html
            )
            self.assertIn("Strength: 1", html)
            self.assertIn("test skill", html)
            self.assertIn("test weapon x 1", html)
            self.assertIn("Barbarian: 1", html)
