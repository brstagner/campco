from flask import Flask
import os
from models.base import connect_db, db
from routes.user_routes import user_routes
from routes.player_routes import player_routes
from routes.campaign_routes import campaign_routes

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

app.register_blueprint(user_routes)
app.register_blueprint(player_routes)
app.register_blueprint(campaign_routes)

app.app_context().push()

connect_db(app)

# db.drop_all()
# db.create_all()