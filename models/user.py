from flask_bcrypt import Bcrypt
from models.base import db

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    @classmethod
    def register(cls, username, email, password):
        """Register user with hashed password and return user"""
        hashed = bcrypt.generate_password_hash(password)
        # Turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode('utf8')
        # Create user instance
        user = cls(username=username, email=email, password=hashed_utf8)
        # Add user to database
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        # Return instance of user with username, email, and hashed password
        return user

    @classmethod
    def authenticate(cls, username, password):
        """
        Validate that user exists and password is correct
        Return user if valid, else return False
        """
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # Return user instance
            return user
        else:
            return False
    
    @classmethod
    def edit(cls, user, new_username, new_email, new_password):
        """Edit user with hashed password and return user"""

        hashed = bcrypt.generate_password_hash(new_password)
        # Turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode('utf8')

        user.username = new_username
        user.email = new_email
        user.password = hashed_utf8

        # Update user in database
        db.session.commit()
        # Return instance of user with username, email, and hashed password
        return user

    # def __repr__(self):
    #     """Show info user"""
    #     user = self
    #     return f'<Username: {self.username}, Password: {self.password}, Email: {self.email}>'

