from models.base import db
from sqlalchemy.dialects.postgresql import JSON

class Player(db.Model):
    __tablename__ = 'players'
    
    player_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    party_notes = db.Column(db.Text)
    player_notes = db.Column(db.Text)
    dm_notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='cascade'), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id', ondelete='cascade'))

    @classmethod
    def create(cls, name, user_id, campaign_id):
        """Create player"""
        player = cls(name=name, user_id=user_id, campaign_id=campaign_id)
        # Add player to database
        db.session.add(player)
        db.session.commit()
        db.session.refresh(player)

        Demo.add(player.player_id)
        Vitals.add(player.player_id)
        Combat.add(player.player_id)
        Spells.add(player.player_id)
        Ability.add(player.player_id)
        Level.add(player.player_id)
        Proficiency.add(player.player_id)
        Items.add(player.player_id)

        db.session.commit()

        # Return player_id
        return player.player_id
    
    @classmethod
    def edit(cls):
        db.session.commit()

class Demo(db.Model):
    __tablename__ = 'demo'

    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)
    
    player_level = db.Column(db.Integer, default=1)
    player_xp = db.Column(db.Integer, default=0)
    race = db.Column(db.JSON, default={"name": "", "desc": ""})
    subrace = db.Column(db.JSON, default={"name": "", "desc": ""})
    job = db.Column(db.JSON, default={"name": "", "desc": ""})
    subjob = db.Column(db.JSON, default={"name": "", "desc": ""})
    alignment = db.Column(db.JSON, default={"name": "", "desc": ""})
    age = db.Column(db.Integer)
    size = db.Column(db.String(20))
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()

    @classmethod
    def add(cls, player_id):
        demo = cls(player_id=player_id)
        db.session.add(demo)

class Vitals(db.Model):
    __tablename__ = 'vitals'
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)
    hp = db.Column(db.JSON, default={"current": 0, "max": 0})
    hd = db.Column(db.ARRAY(JSON))
    conditions = db.Column(db.ARRAY(JSON))
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()

    @classmethod
    def add(cls, player_id):
        vitals = cls(player_id=player_id)
        db.session.add(vitals)

class Combat(db.Model):
    __tablename__ = 'combat'
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)
    attacks = db.Column(db.ARRAY(JSON), default=[]) # ex. [{name: 'Short Sword', throws:1, die:6, number:2},...]
    ac = db.Column(db.Integer, default=0)
    initiative = db.Column(db.Integer, default=0)
    speed = db.Column(db.Integer, default=0)
    inspiration = db.Column(db.Integer, default=0)
    ki = db.Column(db.JSON, default={"current": 0, "max":0})
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()
    
    @classmethod
    def add(cls, player_id):
        combat = cls(player_id=player_id)
        db.session.add(combat)

class Spells(db.Model):
    __tablename__ = 'spells'
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)
    known = db.Column(db.ARRAY(JSON), default=[])
    lv0 = db.Column(db.ARRAY(JSON), default=[])
    lv1 = db.Column(db.ARRAY(JSON), default=[])
    lv2 = db.Column(db.ARRAY(JSON), default=[])
    lv3 = db.Column(db.ARRAY(JSON), default=[])
    lv4 = db.Column(db.ARRAY(JSON), default=[])
    lv5 = db.Column(db.ARRAY(JSON), default=[])
    lv6 = db.Column(db.ARRAY(JSON), default=[])
    lv7 = db.Column(db.ARRAY(JSON), default=[])
    lv8 = db.Column(db.ARRAY(JSON), default=[])
    lv9 = db.Column(db.ARRAY(JSON), default=[])
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()
    
    @classmethod
    def add(cls, player_id):
        spells = cls(player_id=player_id)
        db.session.add(spells)

class Ability(db.Model):
    __tablename__ = 'abilities'

    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)
    strength = db.Column(db.Integer, default=0)
    dexterity = db.Column(db.Integer, default=0)
    constitution = db.Column(db.Integer, default=0)
    intelligence = db.Column(db.Integer, default=0)
    wisdom = db.Column(db.Integer, default=0)
    charisma = db.Column(db.Integer, default=0)
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()
    
    @classmethod
    def add(cls, player_id):
        ability = cls(player_id=player_id)
        db.session.add(ability)

class Level(db.Model):
    __tablename__ = 'levels'
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)

    Barbarian = db.Column(db.Integer, default=0)
    Bard = db.Column(db.Integer, default=0)
    Cleric = db.Column(db.Integer, default=0)
    Druid = db.Column(db.Integer, default=0)
    Fighter = db.Column(db.Integer, default=0)
    Monk = db.Column(db.Integer, default=0)
    Paladin = db.Column(db.Integer, default=0)
    Ranger = db.Column(db.Integer, default=0)
    Rogue = db.Column(db.Integer, default=0)
    Sorcerer = db.Column(db.Integer, default=0)
    Warlock = db.Column(db.Integer, default=0)
    Wizard = db.Column(db.Integer, default=0)

    @classmethod
    def edit(cls):
        db.session.commit()

    @classmethod
    def add(cls, player_id):
        level = cls(player_id=player_id)
        db.session.add(level)

class Proficiency(db.Model):
    __tablename__ = 'proficiencies'

    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)

    # ex. ['Short Sword', 'Shield]
    skills = db.Column(db.ARRAY(JSON), default=[])
    weapons = db.Column(db.ARRAY(JSON), default=[])
    armor = db.Column(db.ARRAY(JSON), default=[])
    tools = db.Column(db.ARRAY(JSON), default=[])
    languages = db.Column(db.ARRAY(JSON), default=[])
    traits = db.Column(db.ARRAY(JSON), default=[])
    features = db.Column(db.ARRAY(JSON), default=[])
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()
    
    @classmethod
    def add(cls, player_id):
        proficiency = cls(player_id=player_id)
        db.session.add(proficiency)

class Items(db.Model):
    __tablename__ = 'items'

    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id', ondelete='cascade'), primary_key=True, unique=True)

    weapons = db.Column(db.ARRAY(JSON), default=[])
    armor = db.Column(db.ARRAY(JSON), default=[])
    tools = db.Column(db.ARRAY(JSON), default=[])
    wallet = db.Column(db.ARRAY(JSON), default=[])
    other = db.Column(db.ARRAY(JSON), default=[])

    weight = db.Column(db.JSON, default={"current": 0, "max": 0})
    notes = db.Column(db.Text)

    @classmethod
    def edit(cls):
        db.session.commit()
    
    @classmethod
    def add(cls, player_id):
        items = cls(player_id=player_id)
        db.session.add(items)