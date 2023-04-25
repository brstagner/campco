from flask import Blueprint, render_template, flash, session, redirect
from forms.player_forms import (
    PlayerCreate,
    EditPlayer,
    EditDemo,
    EditVitals,
    EditCombat,
    EditSpells,
    EditAbility,
    EditProficiency,
    EditItems,
    EditLevel,
)
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
from models.campaign import Campaign
from authorization import edit_auth
from dnd_requests import (
    demo_query,
    vitals_query,
    spells_query,
    proficiency_query,
    items_query,
)

player_routes = Blueprint("player_routes", __name__, template_folder="templates")


@player_routes.route("/player/create", methods=["GET", "POST"])
def create():
    """
    Shows form to create player
    Adds new player to database
    """
    form = PlayerCreate()
    campaigns = Campaign.names()

    if form.validate_on_submit():
        user_id = session["user_id"]
        campaign_id = form.campaign_id.data
        password = form.password.data

        # Authenticate will return a user or False
        campaign = Campaign.authenticate(campaign_id, password)

        if campaign or campaign_id == None:
            # Permit creation
            name = form.name.data
            player_id = Player.create(name, user_id, campaign_id)

            return redirect(f"/player/{player_id}")

        else:
            flash("Authentication failed, check password")
            return redirect(f"/player/create")
    else:
        return render_template("player/create.html", form=form, campaigns=campaigns)


@player_routes.route("/player/<player_id>")
def player_detail(player_id):
    """
    Verify logged-in user owns player
    Render player detail page
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    demo = Demo.query.get(player_id)
    vitals = Vitals.query.get(player_id)
    combat = Combat.query.get(player_id)
    spells = Spells.query.get(player_id)
    ability = Ability.query.get(player_id)
    level = Level.query.get(player_id)
    proficiency = Proficiency.query.get(player_id)
    items = Items.query.get(player_id)
    campaign = Campaign.query.get(player.campaign_id)
    if campaign:
        campaign = campaign.name
    else:
        campaign = None

    return render_template(
        "/player/detail.html",
        edit=True,
        player=player,
        demo=demo,
        vitals=vitals,
        combat=combat,
        spells=spells,
        ability=ability,
        level=level,
        proficiency=proficiency,
        items=items,
        campaign=campaign,
    )


### Player Edit Routes ###


@player_routes.route("/player/<player_id>/edit/player", methods=["GET", "POST"])
def edit_player(player_id):
    """
    Verify player exists and logged-in user owns player
    Render player edit form and update player
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditPlayer()
    player = Player.query.get(player_id)
    current_campaign_id = player.campaign_id
    # campaigns = Campaign.query.all()

    if form.validate_on_submit():
        campaign_id = form.campaign_id.data
        password = form.password.data

        # Authenticate will return a user or False
        campaign = Campaign.authenticate(campaign_id, password)

        if campaign or campaign_id == None or campaign_id == current_campaign_id:
            # Permit edit

            player.name = form.name.data

            if campaign_id != None:
                player.campaign_id = campaign_id
            else:
                player.campaign_id = None

            # commit to database
            Player.edit()

            return redirect(f"/player/{player_id}")

        else:
            flash("Campaign authentication failed, check password")
            return redirect(f"/player/{player_id}/edit/player")

    else:
        form.campaign_id.data = player.campaign_id
        form.name.data = player.name

        return render_template(
            "/player/edit/edit-player.html", form=form, player=player
        )


@player_routes.route("/player/<player_id>/edit/demo", methods=["GET", "POST"])
def edit_demo(player_id):
    """
    Verify logged-in user owns player
    Render demo edit form and update player demo
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditDemo()
    demo = Demo.query.get(player_id)

    if form.validate_on_submit():
        demo.player_level = form.player_level.data
        demo.player_xp = form.player_xp.data
        demo.race = eval(form.race.data)
        demo.subrace = eval(form.subrace.data)
        demo.job = form.job.data
        demo.subjob = eval(form.subjob.data)
        demo.age = form.age.data
        demo.alignment = eval(form.alignment.data)
        demo.size = form.size.data
        demo.notes = form.notes.data

        # commit to database
        Demo.edit()

        return redirect(f"/player/{player_id}")

    else:
        options = demo_query()

        form.player_level.data = demo.player_level
        form.player_xp.data = demo.player_xp
        form.race.data = demo.race
        form.subrace.data = demo.subrace
        form.job.data = demo.job
        form.subjob.data = demo.subjob
        form.age.data = demo.age
        form.alignment.data = demo.alignment
        form.size.data = demo.size
        form.notes.data = demo.notes

        return render_template(
            "/player/edit/edit-demo.html",
            form=form,
            player_id=player_id,
            demo=demo,
            options=options,
        )


@player_routes.route("/player/<player_id>/edit/level", methods=["GET", "POST"])
def edit_level(player_id):
    """
    Verify logged-in user owns player
    Render demo edit form and update player level
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditLevel()
    level = Level.query.get(player_id)

    if form.validate_on_submit():
        level.Barbarian = form.barbarian.data
        level.Bard = form.bard.data
        level.Cleric = form.cleric.data
        level.Druid = form.druid.data
        level.Fighter = form.fighter.data
        level.Monk = form.monk.data
        level.Paladin = form.paladin.data
        level.Ranger = form.ranger.data
        level.Rogue = form.rogue.data
        level.Sorcerer = form.sorcerer.data
        level.Warlock = form.warlock.data
        level.Wizard = form.wizard.data

        # commit to database
        Level.edit()

        return redirect(f"/player/{player_id}")

    else:
        form.barbarian.data = level.Barbarian
        form.bard.data = level.Bard
        form.cleric.data = level.Cleric
        form.druid.data = level.Druid
        form.fighter.data = level.Fighter
        form.monk.data = level.Monk
        form.paladin.data = level.Paladin
        form.ranger.data = level.Ranger
        form.rogue.data = level.Rogue
        form.sorcerer.data = level.Sorcerer
        form.warlock.data = level.Warlock
        form.wizard.data = level.Wizard
        return render_template(
            "/player/edit/edit-level.html", form=form, player_id=player_id
        )


@player_routes.route("/player/<player_id>/edit/vitals", methods=["GET", "POST"])
def edit_vitals(player_id):
    """
    Verify logged-in user owns player
    Render vitals edit form and update player vitals
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditVitals()
    vitals = Vitals.query.get(player_id)

    if form.validate_on_submit():
        vitals.hp = eval(form.hp.data)
        vitals.hd = eval(form.hd.data)
        vitals.conditions = eval(form.conditions.data)
        vitals.notes = form.notes.data

        # commit to database
        Vitals.edit()

        return redirect(f"/player/{player_id}")

    else:
        options = vitals_query()

        if vitals.hp:
            form.hp.data = vitals.hp
        else:
            form.hp.data = {"current": 0, "max": 0}
            form.hd.data = vitals.hd if vitals.hd else {}
            form.conditions.data = vitals.conditions if vitals.conditions else {}
            form.notes.data = vitals.notes

        return render_template(
            "/player/edit/edit-vitals.html",
            form=form,
            player_id=player_id,
            vitals=vitals,
            options=options,
        )


@player_routes.route("/player/<player_id>/edit/combat", methods=["GET", "POST"])
def edit_combat(player_id):
    """
    Verify logged-in user owns player
    Render combat edit form and update player combat
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditCombat()
    combat = Combat.query.get(player_id)
    # attacks = eval(combat.attacks)
    # weapons = eval(Items.query.get(player_id).weapons)

    if form.validate_on_submit():
        combat.attacks = eval(form.attacks.data)
        combat.ac = form.ac.data
        combat.inititative = form.initiative.data
        combat.speed = form.speed.data
        combat.inspiration = form.inspiration.data
        combat.ki = eval(form.ki.data)
        combat.notes = form.notes.data

        # commit to database
        Combat.edit()

        return redirect(f"/player/{player_id}")

    else:
        form.attacks.data = combat.attacks
        form.ac.data = combat.ac
        form.initiative.data = combat.initiative
        form.speed.data = combat.speed
        form.inspiration.data = combat.inspiration
        form.ki.data = combat.ki
        form.notes.data = combat.notes

        return render_template(
            "/player/edit/edit-combat.html",
            form=form,
            player_id=player_id,
            combat=combat,
        )


@player_routes.route("/player/<player_id>/edit/spells", methods=["GET", "POST"])
def edit_spells(player_id):
    """
    Verify logged-in user owns player
    Render spells edit form and update player spells
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditSpells()
    spells = Spells.query.get(player_id)

    if form.validate_on_submit():
        spells.known = eval(form.known.data) or []
        spells.lv0 = eval(form.lv0.data) or []
        spells.lv1 = eval(form.lv1.data) or []
        spells.lv2 = eval(form.lv2.data) or []
        spells.lv3 = eval(form.lv3.data) or []
        spells.lv4 = eval(form.lv4.data) or []
        spells.lv5 = eval(form.lv5.data) or []
        spells.lv6 = eval(form.lv6.data) or []
        spells.lv7 = eval(form.lv7.data) or []
        spells.lv8 = eval(form.lv8.data) or []
        spells.lv9 = eval(form.lv9.data) or []
        spells.notes = form.notes.data

        # commit to database
        Spells.edit()

        return redirect(f"/player/{player_id}")

    else:
        options = spells_query()

        form.known.data = spells.known
        form.lv0.data = spells.lv0
        form.lv1.data = spells.lv1
        form.lv2.data = spells.lv2
        form.lv3.data = spells.lv3
        form.lv4.data = spells.lv4
        form.lv5.data = spells.lv5
        form.lv6.data = spells.lv6
        form.lv7.data = spells.lv7
        form.lv8.data = spells.lv8
        form.lv9.data = spells.lv9
        form.notes.data = spells.notes

        return render_template(
            "/player/edit/edit-spells.html",
            form=form,
            player_id=player_id,
            spells=spells,
            options=options,
        )


@player_routes.route("/player/<player_id>/edit/ability", methods=["GET", "POST"])
def edit_ability(player_id):
    """
    Verify logged-in user owns player
    Render ability edit form and update player ability
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditAbility()
    ability = Ability.query.get(player_id)

    if form.validate_on_submit():
        ability.strength = form.strength.data
        ability.dexterity = form.dexterity.data
        ability.constitution = form.constitution.data
        ability.intelligence = form.intelligence.data
        ability.wisdom = form.wisdom.data
        ability.charisma = form.charisma.data
        ability.notes = form.notes.data

        # commit to database
        Ability.edit()

        return redirect(f"/player/{player_id}")

    else:
        form.strength.data = ability.strength
        form.dexterity.data = ability.dexterity
        form.constitution.data = ability.constitution
        form.intelligence.data = ability.intelligence
        form.wisdom.data = ability.wisdom
        form.charisma.data = ability.charisma
        form.notes.data = ability.notes

        return render_template(
            "/player/edit/edit-ability.html",
            form=form,
            player_id=player_id,
            ability=ability,
        )


@player_routes.route("/player/<player_id>/edit/proficiency", methods=["GET", "POST"])
def edit_proficiency(player_id):
    """
    Verify logged-in user owns player
    Render proficiency edit form and update player proficiency
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditProficiency()
    proficiency = Proficiency.query.get(player_id)

    if form.validate_on_submit():
        proficiency.skills = eval(form.skills.data)
        proficiency.weapons = eval(form.weapons.data)
        proficiency.armor = eval(form.armor.data)
        proficiency.tools = eval(form.tools.data)
        proficiency.languages = eval(form.languages.data)
        proficiency.traits = eval(form.traits.data)
        proficiency.features = eval(form.features.data)
        proficiency.notes = form.notes.data

        # commit to database
        Proficiency.edit()

        return redirect(f"/player/{player_id}")

    else:
        options = proficiency_query()

        form.skills.data = proficiency.skills
        form.weapons.data = proficiency.weapons
        form.armor.data = proficiency.armor
        form.tools.data = proficiency.tools
        form.languages.data = proficiency.languages
        form.traits.data = proficiency.traits
        form.features.data = proficiency.features
        form.notes.data = proficiency.notes

        return render_template(
            "/player/edit/edit-proficiency.html",
            form=form,
            player_id=player_id,
            proficiency=proficiency,
            options=options,
        )


@player_routes.route("/player/<player_id>/edit/items", methods=["GET", "POST"])
def edit_items(player_id):
    """
    Verify logged-in user owns player
    Render items edit form and update player items
    """
    player = edit_auth(player_id)
    if player == None:
        return redirect("/")

    form = EditItems()
    items = Items.query.get(player_id)

    if form.validate_on_submit():
        items.weapons = eval(form.weapons.data)
        items.armor = eval(form.armor.data)
        items.tools = eval(form.tools.data)
        items.wallet = eval(form.wallet.data)
        items.other = eval(form.other.data)
        items.weight = eval(form.weight.data)
        items.notes = form.notes.data

        # commit to database
        Items.edit()

        return redirect(f"/player/{player_id}")

    else:
        options = items_query()

        form.weapons.data = items.weapons
        form.armor.data = items.armor
        form.tools.data = items.tools
        form.wallet.data = items.wallet
        form.other.data = items.other
        form.weight.data = items.weight
        form.notes.data = items.notes

        return render_template(
            "/player/edit/edit-items.html",
            form=form,
            player_id=player_id,
            items=items,
            options=options,
        )
