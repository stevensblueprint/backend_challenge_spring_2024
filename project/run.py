from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import uuid
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

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

class Volunteer(db.Model, SerializerMixin):
    __tablename__ = "volunteers"
    volunteer_id = db.Column(db.UUID, primary_key=True)
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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})
    
@app.route("/api/volunteers", methods=["GET"])
def list_volunteers():
    pagination_from = request.args.get("pagination-from")
    pagination_to = request.args.get("pagination-to")
    filtering = request.args.get("filter-by-skill")
    sorting = request.args.get("sort")
    volunteers = ""
    if pagination_from == None:
        volunteers = Volunteer.query.all()
    else:
        volunteers = Volunteer.query(Volunteer.engine.execute("SELECT * FROM volunteers LIMIT " + pagination_from + ", " + pagination_to))
    volunteer_list = [{"volunteer_id":v.volunteer_id, 
                       "first_name":v.first_name, 
                       "last_name":v.last_name, 
                       "email":v.email, 
                       "phone_number":v.phone_number, 
                       "date_of_birth":v.date_of_birth, 
                       "address":v.address, 
                       "skills":v.skills, 
                       "availability":v.availability, 
                       "date_joined":v.date_joined, 
                       "background_check":v.background_check}
                      for v in volunteers]

    def filterRule(entry):
        if filtering in (entry["skills"])[1:-2].split(','): # Converts a JSON array in the format [x, y, z] to a Python array
            return True
        return False
    
    if filtering != None:
        volunteer_list = list(filter(filterRule, volunteer_list))

    def sortHandler(entry):
        return entry["first_name"]

    if sorting == "asc":
        volunteer_list = sorted(volunteer_list, sortHandler, False)

    if sorting == "dsc":
        volunteer_list = sorted(volunteer_list, sortHandler, True)

    print(volunteer_list)
    return jsonify(volunteer_list)

@app.route("/api/volunteers", methods=["POST"])
def new_volunteer():
    # fetch the json from the request body via flask
    data = request.get_json()
    # validate the json (check if thngs that supposed to be numbers are numbers, etc.. (optional)
    # genrate uuid for the primary key
    uid = uuid.uuid4()
    # insert the data to the datbase

    newv = Volunteer(volunteer_id=uid,
                     first_name=data["first_name"],
                     last_name=data["last_name"],
                     email=data["email"],
                     phone_number=data["phone_number"],
                     date_of_birth=datetime.strptime(data["date_of_birth"], "%Y-%m-%d"),
                     address=data["address"],
                     skills=data["skills"],
                     availability=data["availability"],
                     date_joined=datetime.now(),
                     background_check=data["background_check"]
                     )

    db.session.add(newv)
    db.session.commit()

    return jsonify({"message": uid}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
