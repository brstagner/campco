# Integrated D&D Game Manager

## Setup:

1. Install required packages.
2. Create .env file with DATABASE_URL and SECRET_KEY variables.

## Goal:

Provide basic web-based player and campaign management for Dungeons and Dragons 5e games. All users should be able to participate with a smartphone, tablet, or PC; either in person or remotely (with dialogue via Zoom, Skype, chat app support). Fill a gap between apps that handle one part of the game (character or campaign creation) but are not integrated, and apps that are graphics-heavy and cumbersome.

## Data:

Game rulebook data from dnd5eapi (https://www.dnd5eapi.co/docs/).

This data is available as part of the 'System Reference Document 5.1 (“SRD5”)' granted through use of the Open Gaming License, Version 1.0a.

Data is accessed via GraphQL (https://www.dnd5eapi.co/graphql).

This includes the basic rule set for D&D 5e games (player races, classes, monsters, combat mechanics, etc.). It should be sufficient for full character creation and equipping, tracking stats (XP, level, etc.), and building campaigns.

User-saved data (users, players, campaigns) is hosted on a postgres database at supabase.com.

## Functionality:

App should permit creation and editing of player characters (PCs) and campaigns. App should collect players into a single campaign, run by a single user (the 'dungeon master' or 'DM'). DMs should get access to player information without ability to edit. Players should get access to all of their own data, plus select data from other players in the campaign, as permitted by those players.

## This project was built using:

- Flask
- Bcrypt
- SQLAlchemy
- WTForms
