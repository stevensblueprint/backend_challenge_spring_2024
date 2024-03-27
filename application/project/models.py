from project import db

class Volunteer(db.model):
    __tablename__ = "Volunteers"
    volunteer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    date_of_birth = db.Column(db.DateTime)
    address = db.Column(db.String(255))
    skills = db.Column(db.String(255)) # Will be jsonified
    availability = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime)
    back-ground_check = db.Column(db.Boolean)
