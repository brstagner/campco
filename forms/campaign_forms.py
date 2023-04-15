from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, EqualTo

class CreateCampaign(FlaskForm):
    name = StringField('Name (required)', validators=[InputRequired(message='Name cannot be blank')])
    password = PasswordField('Password (required)', validators=[InputRequired(message='Password cannot be blank'), EqualTo('repassword', message='Passwords must match')])
    repassword = PasswordField('Reenter Password')
    description = TextAreaField('Description')

class EditCampaign(FlaskForm):
    name = StringField('Name (required)', validators=[InputRequired(message='Name cannot be blank')])
    description = TextAreaField('Description')