#To start server
#cd Desktop/Blueprint/backend_challenge_spring_2024
#C:\Users\Lucas\Desktop\Blueprint\backend_challenge_spring_2024>uvicorn main:app --reload


import datetime
from pydantic import BaseModel
from pydantic import ConfigDict
from fastapi import FastAPI


app = FastAPI()

class volunteer(BaseModel):
    #model_config = ConfigDict(from_attributes=True) #black magic from stackoverflow https://stackoverflow.com/questions/69504352/fastapi-get-request-results-in-typeerror-value-is-not-a-valid-dict

    volunteer_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    date_of_birth: str #maybe date?
    #date_of_birth: datetime 
    address: str
    skills: list #list of strings
    availability: list #maybe calander or list of datetimes
    date_joined: str #maybe date?
    #date_joined: datetime 
    background_check: bool

# today = date.today() - - - get todays date
    
#dictionary of all volunteers. volunteer id is used as each volunteers key in the dictionary
volunteers = {
    0: volunteer(
        volunteer_id = 0,
        first_name="Lucas", 
        last_name="Brusa", 
        email="example", 
        phone_number=555, 
        date_of_birth= "01222004",
        address = "1 First Street, Origin, NY 00000",
        skills = ["fun", "handsome", "enjoys long walks on the beach"],
        availability = ["Monday", "Tuesday", "Wednesday", "Friday"],
        date_joined = "04012024",
        background_check = False
        ),
}


# Retrieves a list of all volunteers, no options for pagination, filtering, or sorting.
@app.get("/")
def index() -> dict[str, dict[int, volunteer]]:
    return{"volunteers": volunteers}


# Creates a new volunteer record.
@app.post("/")
def add_volunteer(volunteer: volunteer) -> dict[str, volunteer]:

    if volunteer.volunteer_id in volunteers:
        raise BaseException(
            status_code=400, 
            detail=f"Item  with {volunteer.volunteer_id=} already exists."
            )

    volunteers[volunteer.volunteer_id] = volunteer # updates the volunteer whose id (key) was specified
    return {"added": volunteer}


# Retrieves detailed information about a specific volunteer via their ID.
@app.get("/volunteers/{volunteer_id}")
def query_by_id(volunteer_id: int) -> volunteer:
    if volunteer_id not in volunteers:
        raise BaseException(
            status_code=404, 
            detail=f"Volunteer with {volunteer_id=} does not exists."
            )
    return volunteers[volunteer_id] #returns the specified volunteer by retrieving it via its id (key)


# Retrieves detailed information about a specific volunteer. (doesnt work for some reason)
Selection = dict[str, str | int | list | bool | None] # a dictionary where the keys are of type 'str' and the values are either str, int, list, bool, or None. Corresponding to the possible types given by the volunteer class
@app.get("/volunteers/")
def query_by_anyData(
    volunteer_id: int | None = None,
    first_name: str | None = None, # string OR None, means it can be empty (ie an optional query parameter)
    last_name: str | None = None,
    email: str | None = None,
    phone_number: str | None = None,
    date_of_birth: str | None = None,
    address: str | None = None,
    skills: list | None = None,
    availability: list | None = None,
    date_joined: str | None = None,
    background_check: bool | None = None
) -> dict[str, Selection]: # returns a dictionary where the keys are of type 'str' and the values are of type 'Selection'
    def check_volunteer(queried: volunteer) -> bool:
        return all( # python "all" checks all conditions and returns true if all conditions are true
            (
                volunteer_id is None or queried.volunteer_id == volunteer_id,
                first_name is None or queried.first_name == first_name,
                last_name is None or queried.last_name == last_name,
                email is None or queried.email == email,
                phone_number is None or queried.phone_number == phone_number,
                date_of_birth is None or queried.date_of_birth == date_of_birth,
                address is None or queried.address == address,
                skills is None or queried.skills == skills,
                availability is None or queried.availability == availability,
                date_joined is None or queried.date_joined == date_joined,
                background_check is None or queried.background_check == background_check,
            )
        )
    selection = [volunteer for volunteer in volunteers.values() if check_volunteer(volunteer)] # iterates through volunteers and creates a new list of volunteers if their values match those given by the function's parameters
    
    return {
        # return original query
        "query": {"id": volunteer_id,
                  "first name": first_name,
                  "last name": last_name,
                  "email": email,
                  "phone number": phone_number,
                  "DOB": date_of_birth,
                  "address": address,
                  "skills": skills,
                  "availability": availability,
                  "date joined": date_joined,
                  "background check": background_check
                  },
        # return found volunteer as well
        "selection": selection,
    }



# Updates an existing volunteer's information.
@app.put("/volunteers/{volunteer_id}")
def update(
    volunteer_id: int,
    first_name: str | None = None, # string OR None means it can be empty (ie. an optional query parameter)
    last_name: str | None = None,
    email: str | None = None,
    phone_number: str | None = None,
    date_of_birth: str | None = None,
    address: str | None = None,
    skills: list | None = None,
    availability: list | None = None,
    date_joined: str | None = None,
    background_check: bool | None = None
) -> dict[str, volunteer]: # returns a dictionary where the keys are of type 'str' and the values are of type 'volunteer'
    if volunteer_id not in volunteers:
        raise BaseException(
            status_code=404, 
            detail=f"Volunteer with {volunteer_id=} does not exists."
            )
    if all(info is None for info in (volunteer_id, first_name, last_name, email, phone_number, date_of_birth, address, skills, availability, date_joined, background_check)):
        raise BaseException(
            status_code=400, 
            detail="No parameters provided for update."
            )
    
    volunteer = volunteers[volunteer_id]
    if volunteer_id is not None:
        volunteer.volunteer_id = volunteer_id
    if first_name is not None:
        volunteer.first_name = first_name
    if last_name is not None:
        volunteer.last_name = last_name
    if email is not None:
        volunteer.email = email
    if phone_number is not None:
        volunteer.phone_number = phone_number
    if date_of_birth is not None:
        volunteer.date_of_birth = date_of_birth
    if address is not None:
        volunteer.address = address
    if skills is not None:
        volunteer.skills = skills
    if availability is not None:
        volunteer.availability = availability
    if date_joined is not None:
        volunteer.date_joined = date_joined
    if background_check is not None:
        volunteer.background_check = background_check

    return {"updated": volunteer}


#Deletes a specific volunteer's record.
@app.delete("/volunteers/{volunteer_id}")
def delete_volunteer(volunteer_id: int) -> dict[str, volunteer]:

    if volunteer_id not in volunteers:
        raise BaseException(
            status_code=404, 
            detail=f"Volunteer with {volunteer_id=} does not exists."
            )
    
    volunteer = volunteers.pop(volunteer_id) # removed a volunteer from the dictionary of volunteers based on the specified id (key)
    return {"deleted": volunteer}
