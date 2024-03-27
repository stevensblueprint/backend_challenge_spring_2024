from flask import Blueprint, jsonify, request
from project import db
from project.models import Volunteer

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
                       "back-ground_check":v.back-ground_check} \
                      for v in volunteers]
    
    
