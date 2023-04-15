from flask_bcrypt import Bcrypt
from models.base import db

bcrypt = Bcrypt()

class Campaign(db.Model):
    __tablename__ = 'campaigns'

    campaign_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='cascade'))

    @classmethod
    def create(cls, user_id, name, password, description):
        """Create campaign with hashed password and return campaign_id"""
        hashed = bcrypt.generate_password_hash(password)
        # Turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode('utf8')

        campaign = cls(user_id=user_id, name=name, password=hashed_utf8, description=description)

        db.session.add(campaign)
        db.session.commit()

        db.session.refresh(campaign)

        # Return instance of campaign with campaign_id and hashed password
        return campaign.campaign_id

    @classmethod
    def authenticate(cls, campaign_id, password):
        """
        Validate that campaign exists and password is correct
        Return campaign if valid, else return False
        """
        campaign = Campaign.query.filter_by(campaign_id=campaign_id).first()
        if campaign and bcrypt.check_password_hash(campaign.password, password):
            # Return user instance
            return campaign
        else:
            return False
        
    @classmethod
    def edit(cls):
        db.session.commit()
    
    @classmethod
    def names(cls):
        campaigns = Campaign.query.all()
        campaigns = [{"name": campaign.name, "campaign_id": campaign.campaign_id} for campaign in campaigns]
        return campaigns