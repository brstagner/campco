from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Optional

class PlayerCreate(FlaskForm):
    """
    Model for form object with all fields for adding new users to database
    """
    campaign_id = IntegerField('Campaign ID #', validators=[Optional()])
    password = PasswordField('Campaign Password (required if selecting a campaign)')
    name = StringField('Player Name (required)', validators=[InputRequired(message='Name cannot be blank')])

class EditPlayer(FlaskForm):
    campaign_id = IntegerField('Campaign', validators=[Optional()])
    password = PasswordField('Campaign Password (required if selecting a campaign)')
    name = StringField('Name', validators=[InputRequired(message='Name cannot be blank')])

class EditDemo(FlaskForm):
    player_level = IntegerField('Player Level')
    player_xp = IntegerField('Player XP')
    race = StringField('Race')
    subrace = StringField('Subrace')
    job = StringField('Job')
    subjob = StringField('Subjob')
    age = IntegerField('Age')
    alignment = StringField('Alignment')
    size = StringField('Size')
    notes = TextAreaField('Notes')

class EditLevel(FlaskForm):
    barbarian = IntegerField('Barbarian lv.')
    bard = IntegerField('Bard lv.')
    cleric = IntegerField('Cleric lv.')
    druid = IntegerField('Druid lv.')
    fighter = IntegerField('Fighter lv.')
    monk = IntegerField('Monk lv.')
    paladin = IntegerField('Paladin lv.')
    ranger = IntegerField('Ranger lv.')
    rogue = IntegerField('Rogue lv.')
    sorcerer = IntegerField('Sorcerer lv.')
    warlock = IntegerField('Warlock lv.')
    wizard = IntegerField('Wizard lv.')

    notes = TextAreaField('Notes')

class EditVitals(FlaskForm):
    hp = StringField('HP')
    hd = StringField('HD')
    conditions = StringField('Conditions')
    notes = TextAreaField('Vitals Notes')

class EditCombat(FlaskForm):
    attacks = StringField('Attacks')
    ac = IntegerField('AC')
    initiative = IntegerField('Initiative')
    speed = IntegerField('Speed')
    inspiration = IntegerField('Inspiration')
    ki = StringField('Ki')
    notes = TextAreaField('Combat Notes')

class EditSpells(FlaskForm):
    known = StringField('Known Spells')
    lv0 = StringField('Level 0')
    lv1 = StringField('Level 1')
    lv2 = StringField('Level 2')
    lv3 = StringField('Level 3')
    lv4 = StringField('Level 4')
    lv5 = StringField('Level 5')
    lv6 = StringField('Level 6')
    lv7 = StringField('Level 7')
    lv8 = StringField('Level 8')
    lv9 = StringField('Level 9')
    notes = TextAreaField('Spell Notes')

class EditAbility(FlaskForm):
    strength = IntegerField('Strength')
    dexterity = IntegerField('Dexterity')
    constitution = IntegerField('Constitution')
    intelligence = IntegerField('Intelligence')
    wisdom = IntegerField('Wisdom')
    charisma = IntegerField('Charisma')
    notes = TextAreaField('Ability Notes')

class EditProficiency(FlaskForm):
    skills = StringField('Skills')
    weapons = StringField('Weapons')
    armor = StringField('Armor')
    tools = StringField('Tools')
    languages = StringField('Lanuages')
    traits = StringField('Traits')
    features = StringField('Features')
    notes = TextAreaField('Proficiency Notes')

class EditItems(FlaskForm):
    weapons = StringField('Weapons')
    armor = StringField('Armor')
    tools = StringField('Tools')
    wallet = StringField('Wallet')
    other = StringField('Other')
    weight = StringField('Weight')
    notes = TextAreaField('Items Notes')

