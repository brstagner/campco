# Integrated D&D Game Manager

## Overview:

Provides basic web-based player and campaign management for Dungeons and Dragons 5e games. All users should be able to participate with a smartphone, tablet, or PC; either in person or remotely (with dialogue via Zoom, Skype, chat app support). Fills a gap between apps that handle one part of the game (character or campaign creation) but are not integrated, and apps that are graphics-heavy and cumbersome.

## Data:

Game rulebook data from dnd5eapi (https://www.dnd5eapi.co/docs/).

This data is available as part of the 'System Reference Document 5.1 (“SRD5”)' granted through use of the Open Gaming License, Version 1.0a.

Data is accessed via GraphQL (https://www.dnd5eapi.co/graphql).

This includes the basic rule set for D&D 5e games (player races, classes, monsters, combat mechanics, etc.). It should be sufficient for full character creation and equipping, tracking stats (XP, level, etc.), and building campaigns.

User-saved data (users, players, campaigns) is hosted on a postgres database at supabase.com.

## Functionality:

Permits creation and editing of player characters ('PCs') and campaigns. Collect multiple players (the 'party') into a single campaign, run by a single user (the 'dungeon master' or 'DM'). DMs and party members should get access to player information, without ability to edit, for players they don't own. Users should get access to all of their own players' data with editing privileges.

## Setup:
1. Install required packages:
    >```$ pip3 install -r requirements.txt```
2. Create .env file with these variables:
    >```DATABASE_URL = "[Your production database connection string]"```  
    >```TEST_DATABASE_URL = "[Your test database connection string]"```  
    >```SECRET_KEY = "[A secret key]"```  
    >```WTF_CSRF_ENABLED = "True"```
3. If this is the first deployment or you've made changes to the database object models, and you want to (re)create the tables, uncomment lines 30 & 31 in app.py (```db.drop_all(), db.create_all()```). Comment out those lines again for subsequent deployments to prevent losing data saved in the database.

## Deployment:
Local:
- This app uses a PostgreSQL database. If you'd like to set up a local database, the docs are here: https://www.postgresql.org/.
- Command: ```$ flask run```  
- Direct browser to "localhost:500"  

Remote:
- The deployment of this app at https://campco.onrender.com/ uses a database hosted at https://supabase.com/.
- ```$ gunicorn -w 4 app:app```  
- Add "--threads" flag to give workers more threads (default is 1), adjust number of workers as necessary.

## Testing:
Run tests: ```$ python3 -m unittest discover tests```

## This project was built using:

- Flask: https://flask.palletsprojects.com/en/2.2.x/
- SQLAlchemy: https://www.sqlalchemy.org/
- Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
- WTForms: https://wtforms.readthedocs.io/en/3.0.x/
- Flask WTF: https://flask-wtf.readthedocs.io/en/1.0.x/
- Jinja: https://jinja.palletsprojects.com/en/3.1.x/
- Flask-Bcrypt: https://flask-bcrypt.readthedocs.io/en/1.0.1/
