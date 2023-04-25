from flask import Blueprint, render_template, flash, session, redirect
from forms.campaign_forms import CreateCampaign, EditCampaign
from models.campaign import Campaign
from models.user import User
from models.player import (
    Player,
    Demo,
    Vitals,
    Combat,
    Spells,
    Ability,
    Level,
    Proficiency,
    Items,
)

campaign_routes = Blueprint("campaign_routes", __name__, template_folder="templates")


@campaign_routes.route("/campaign/create", methods=["GET", "POST"])
def create_campaign():
    """
    Shows form to create campaign
    Adds a new campaign to database
    """
    if "user_id" not in session:
        flash("Log in to create a campaign")
        return redirect("/")

    form = CreateCampaign()
    user_id = session["user_id"]

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        password = form.password.data

        campaign_id = Campaign.create(user_id, name, password, description)

        return redirect(f"/campaign/{campaign_id}")
    else:
        return render_template("campaign/create.html", form=form)


@campaign_routes.route("/campaign/<campaign_id>")
def dm_campaign_view(campaign_id):
    """
    Verify logged-in user owns campaign
    Render campaign page (DM view)
    """
    campaign = Campaign.query.get(campaign_id)

    if campaign == None:
        flash("Not authorized to view this campaign")
        return redirect("/")

    players = Player.query.filter(Player.campaign_id == campaign_id).all()
    user_ids = [player.user_id for player in players]

    if "user_id" not in session or (
        session["user_id"] not in user_ids and campaign.user_id != session["user_id"]
    ):
        flash(f"Not authorized to view this campaign")
        return redirect("/")

    if session["user_id"] == campaign.user_id:
        dm = True
    else:
        dm = False

    return render_template(
        "/campaign/detail.html", dm=dm, campaign=campaign, players=players
    )


@campaign_routes.route("/campaign/<campaign_id>/edit", methods=["GET", "POST"])
def edit_campaign(campaign_id):
    """
    Shows form to edit campaign
    Updates campaign in database
    """
    form = EditCampaign()
    campaign = Campaign.query.get(campaign_id)

    if campaign == None:
        flash("Not authorized to edit this campaign")
        return redirect("/")

    user_id = campaign.user_id

    if "user_id" not in session or user_id != session["user_id"]:
        flash("Not authorized to edit this campaign")
        return redirect("/")

    if form.validate_on_submit():
        campaign.name = form.name.data
        campaign.description = form.description.data

        Campaign.edit()

        return redirect(f"/campaign/{campaign.campaign_id}")
    else:
        form.name.data = campaign.name
        form.description.data = campaign.description
        return render_template(
            "campaign/edit-campaign.html",
            form=form,
            campaign=campaign,
        )


@campaign_routes.route("/campaign/party/<player_id>")
def player_detail(player_id):
    """
    Verify logged-in user owns player
    Render player detail page
    """
    ## CHECK FOR PARTY MEMBER OR DM HERE
    # player = edit_auth(player_id)
    # if player == None:
    #     return redirect('/')

    player = Player.query.get(player_id)

    demo = Demo.query.get(player_id)
    vitals = Vitals.query.get(player_id)
    combat = Combat.query.get(player_id)
    spells = Spells.query.get(player_id)
    ability = Ability.query.get(player_id)
    level = Level.query.get(player_id)
    proficiency = Proficiency.query.get(player_id)
    items = Items.query.get(player_id)

    return render_template(
        "/player/detail.html",
        player=player,
        demo=demo,
        vitals=vitals,
        combat=combat,
        spells=spells,
        ability=ability,
        level=level,
        proficiency=proficiency,
        items=items,
    )
