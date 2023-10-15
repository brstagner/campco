from flask import Blueprint, render_template, flash, session, redirect, request
from forms.user_forms import RegisterUser, LoginUser, EditUser
from models.user import User
from models.campaign import Campaign
from models.player import Player

user_routes = Blueprint("user_routes", __name__, template_folder="templates")


@user_routes.route("/")
def show():
    if "user_id" in session:
        return redirect("/user")
    else:
        return redirect("/login")


# @user_routes.route("/register", methods=["GET", "POST"])
# def register():
#     """
#     Shows form to add users
#     Adds a new user to database
#     """

#     if "user_id" in session:
#         flash("Log out before registering a new user")
#         return redirect("/user")

#     form = RegisterUser()

#     if form.validate_on_submit():
#         username = form.username.data
#         email = form.email.data
#         user_check = User.query.filter(User.username == username).first()
#         email_check = User.query.filter(User.email == email).first()

#         if user_check or email_check:
#             if user_check:
#                 flash("Username already in use, choose a different username")
#             if email_check:
#                 flash("Email already in use")
#             return redirect("/register")

#         password = form.password.data

#         user = User.register(username, email, password)

#         session["username"] = user.username
#         session["user_id"] = user.user_id
#         return redirect("/user")
#     else:
#         print()
#         return render_template("user/register.html", form=form)


@user_routes.route("/register", methods=["GET"])
def show_registration_form():
    """
    Shows the registration form
    """
    if "user_id" in session:
        flash("Log out before registering a new user")
        return redirect("/user")

    form = RegisterUser()
    return render_template("user/register.html", form=form)


@user_routes.route("/register", methods=["POST"])
def process_registration_form():
    """
    Processes the registration form submission
    """
    if "user_id" in session:
        flash("Log out before registering a new user")
        return redirect("/user")

    form = RegisterUser()

    print(f"form.username.data: {form.username.data}")

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        user_check = User.query.filter(User.username == username).first()
        email_check = User.query.filter(User.email == email).first()

        if user_check or email_check:
            if user_check:
                flash("Username already in use, choose a different username")
            if email_check:
                flash("Email already in use")
            return redirect("/register")

        password = form.password.data

        user = User.register(username, email, password)

        session["username"] = user.username
        session["user_id"] = user.user_id
        return redirect("/user")
    else:
        print("form was not validated")

    return render_template("user/register.html", form=form)


# @user_routes.route("/registerone", methods=["POST"])
# def register_one():
#     """
#     Shows form to add users
#     Adds a new user to database
#     """
#     print(request.args.get("username"))
#     print(request.args.get("email"))
#     print(request.args.get("password"))

#     user = User.register(
#         request.args.get("username"),
#         request.args.get("email"),
#         request.args.get("password"),
#     )

#     return "success"

    # user = User.register("ccccc", email, password)


@user_routes.route("/login", methods=["GET", "POST"])
def login():
    """
    Renders login page (username and password form)
    Redirects to user detail page
    """

    if "user_id" in session:
        return redirect("/user")

    form = LoginUser()

    if form.validate_on_submit():
        username = (form.username.data,)
        password = form.password.data

        # Authenticate will return a user or False
        user = User.authenticate(username, password)

        print(user.username)

        if user:
            # Keep logged in
            session["username"] = user.username
            session["user_id"] = user.user_id
            return redirect("/user")
        else:
            form.username.errors = ["Bad username or password"]
            return render_template("user/login.html", form=form)

    return render_template("user/login.html", form=form)


# @user_routes.route("/userone", methods=["GET"])
# def show_user_one():
#     """
#     Redirects to user one detail page
#     """
#     # if "user_id" in session:
#     user = User.query.get(1)
#     players = Player.query.filter(Player.user_id == user.user_id).all()
#     campaigns = Campaign.query.filter(Campaign.user_id == user.user_id).all()
#     return render_template(
#         "user/detail.html", user=user, players=players, campaigns=campaigns
#     )

    # else:
    #     flash("Log in to see user details")
    #     return redirect("/")


@user_routes.route("/user", methods=["GET"])
def show_user():
    """
    Redirects to user detail page
    """
    if "user_id" in session:
        user = User.query.get(session["user_id"])
        players = Player.query.filter(Player.user_id == user.user_id).all()
        campaigns = Campaign.query.filter(Campaign.user_id == user.user_id).all()
        return render_template(
            "user/detail.html", user=user, players=players, campaigns=campaigns
        )

    else:
        flash("Log in to see user details")
        return redirect("/")


@user_routes.route("/user/edit", methods=["GET", "POST"])
def edit_user():
    """
    Renders user edit page
    Updates user information in the database
    """

    if "user_id" in session:
        user = User.query.get(session["user_id"])
    else:
        return redirect("/")

    form = EditUser()

    if form.validate_on_submit():
        user_check = User.query.filter(User.username == form.new_username.data).first()
        email_check = User.query.filter(User.email == form.new_email.data).first()

        if (user_check and user_check.user_id != session["user_id"]) or (
            email_check and email_check.user_id != session["user_id"]
        ):
            if user_check:
                flash("Username already in use, choose a different username")
            if email_check:
                flash("Email already in use")
            return redirect("/user")

        current_password = form.current_password.data

        # Authenticate will return a user or False
        authorized = User.authenticate(user.username, current_password)

        if authorized:
            # Permit edits
            new_username = form.new_username.data
            new_email = form.new_email.data
            new_password = (
                form.new_password.data if form.new_password.data else current_password
            )

            User.edit(user, new_username, new_email, new_password)

            session["username"] = new_username

            return redirect("/user")

        else:
            flash("Authentication failed, check password")
            return redirect("/user/edit")
    else:
        form.new_username.data = user.username
        form.new_email.data = user.email

        return render_template("user/edit-user.html", form=form, user=user)


@user_routes.route("/logout")
def logout():
    """
    Clear any information from the session
    Redirect to ('/')
    """
    if "username" in session:
        session.pop("username")
    if "user_id" in session:
        session.pop("user_id")
    return redirect("/")
