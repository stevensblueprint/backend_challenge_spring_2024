from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Config:
    SECRET_KEY = "QhNDVcwfbBxxcCIvt1KTRpnJ"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mysecretpassword@172.17.0.2"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(model_class=Base)
db.init_app(app)

with app.app_context():
    db.create_all()

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
    background_check = db.Column(db.Boolean)

volun_bp = Blueprint("api/volunteers", __name__)

@volun_bp.route("/api/volunteers", methods=["GET"])
def list_volunteers():
    pagination_from = request.args.get("pagination-from")
    pagination_to = request.args.get("pagination-to")
    filtering = request.args.get("filter")
    sorting = request.args.get("sort")
    volunteers
    if pagination == "":
        volunteers = Volunteer.query.all()
    else:
        volunteers = Volunteer.get_or_404(Volunteer.engine.execute("SELECT * FROM volunteers LIMIT " + pagination_from + ", " + pagination_to))
    volunteer_list = [{"volunteer_id":v.volunteer_id, \
                       "first_name":v.first_name, \
                       "last_name":v.last_name, \
                       "email":v.email, \
                       "phone_number":v.phone_number, \
                       "date_of_birth":v.date_of_birth, \
                       "address":v.address, "skills":v.skills, \
                       "availability":v.availability, \
                       "date_joined":v.date_joined, \
                       "background_check":v.background_check} \
                      for v in volunteers]
