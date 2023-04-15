from flask import flash, session
from models.player import Player

def edit_auth(player_id):

    player = Player.query.get(player_id)

    if player == None:
        flash('Not authorized to view this player')
        return None
    
    user_id = Player.query.get(player_id).user_id

    if user_id != session['user_id']:
        flash('Not authorized to view this player')
        return None
    
    return player