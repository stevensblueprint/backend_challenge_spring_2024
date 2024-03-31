from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import uuid
from datetime import datetime
from operator import itemgetter

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

class Volunteer(db.Model):
    __tablename__ = "volunteers"
    volunteer_id = db.Column(db.UUID, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    date_of_birth = db.Column(db.DateTime)
    address = db.Column(db.String(255))
    skills = db.Column(db.String(255))
    availability = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime)
    background_check = db.Column(db.Boolean)

class Events(db.Model):
    __tablename__ = "events"
    volunteer_id = db.Column(db.UUID, primary_key=True)
    events = db.Column(db.String(255))
    
@app.route("/api/volunteers", methods=["GET"])
def list_volunteers():
    pagination_from = request.args.get("pagination-from")
    pagination_to = request.args.get("pagination-to")
    filtering = request.args.get("filter-by-skill")
    sorting = request.args.get("sort")
    volunteers = Volunteer.query.all()
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

    if pagination_from != None and pagination_to != None:
        volunteer_list = volunteer_list[int(pagination_from):int(pagination_to)]

    def filterRule(entry):
        if filtering in (entry["skills"])[1:-1].split(','): # Converts a JSON array in the format [x, y, z] to a Python array
            return True
        return False
    
    if filtering != None:
        volunteer_list = list(filter(filterRule, volunteer_list))

    def sortHandler(entry):
        return entry["first_name"]

    if sorting == "asc":
        volunteer_list = sorted(volunteer_list, key=itemgetter("first_name"))

    if sorting == "dsc":
        volunteer_list = sorted(volunteer_list, key=itemgetter("first_name"), reverse=True)

    return jsonify(volunteer_list)

@app.route("/api/volunteers", methods=["POST"])
def new_volunteer():
    data = request.get_json()
    vid = uuid.uuid4()

    newv = Volunteer(volunteer_id=vid,
                     first_name=data["first_name"],
                     last_name=data["last_name"],
                     email=data["email"],
                     phone_number=data["phone_number"],
                     date_of_birth=datetime.strptime(data["date_of_birth"], "%Y-%m-%d"),
                     address=data["address"],
                     skills=data["skills"],
                     availability="\"" + str(data["availability"]) +"\"",
                     date_joined=datetime.now(),
                     background_check=data["background_check"]
                     )
    db.session.add(newv)
    db.session.commit()

    return jsonify({"UUID": vid}), 201

@app.route("/api/volunteers/<uuid:volunteerID>", methods=["GET"])
def get_volunteer(volunteerID):
    v = db.get_or_404(Volunteer, volunteerID)
    output = {"volunteer_id":v.volunteer_id, 
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
    return jsonify(output)

@app.route("/api/volunteers/<uuid:volunteerID>", methods=["PUT"])
def mod_volunteer(volunteerID):
    v = db.get_or_404(Volunteer, volunteerID)
    data = request.get_json()
    modv = {"volunteer_id":v.volunteer_id, 
                       "first_name":data["first_name"], 
                       "last_name":data["last_name"], 
                       "email":data["email"], 
                       "phone_number":data["phone_number"], 
                       "date_of_birth":data["date_of_birth"], 
                       "address":data["address"], 
                       "skills":data["skills"], 
                       "availability":"\"" + str(data["availability"]) +"\"", 
                       "background_check":data["background_check"]}
    for k in list(modv.keys()):
        # set the database entry at the key k to the value at the same key in the modified entry
        setattr(v, k, modv[k])
    db.session.commit()
    return jsonify(modv), 201

@app.route("/api/volunteers/<uuid:volunteerID>", methods=["DELETE"])
def del_volunteer(volunteerID):
    v = db.get_or_404(Volunteer, volunteerID)
    db.session.delete(v)
    db.session.commit()
    return jsonify({"messsage":"Successly removed entry with UUID " + str(volunteerID)}), 201

@app.route("/api/volunteers/<uuid:volunteerID>/skills", methods=["GET"])
def get_skills(volunteerID):
    v = db.get_or_404(Volunteer, volunteerID)
    skills = v.skills[1:-1].split(',')
    return jsonify(skills), 201

@app.route("/api/volunteers/<uuid:volunteerID>/skills", methods=["POST"])
def add_skill(volunteerID):
    v = db.get_or_404(Volunteer, volunteerID)
    data = request.get_json()
    skills = v.skills[1:-1].split(',')
    for s in data:
        skills += [s]
    setattr(v, "skills", skills)
    db.session.commit()
    return jsonify(skills), 201

@app.route("/api/volunteers/<uuid:volunteerID>/skills/<string:skillID>", methods=["DELETE"])
def remove_skill(volunteerID, skillID):
    v = db.get_or_404(Volunteer, volunteerID)
    skills = v.skills[1:-1].split(',')
    if skillID in skills:
        skills = skills[0:skills.index(skillID)] + skills[(skills.index(skillID) + 1):]
        setattr(v, "skills", skills)
        db.session.commit()
        return jsonify(skills), 201
    return jsonify({"error":"No skill found for voluneteer titled '" + str(skillID) + "'"}), 404

@app.route("/api/volunteers/<uuid:volunteerID>/events", methods=["GET"])
def get_events(volunteerID):
    e = db.get_or_404(Events, volunteerID)
    return e.events, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
