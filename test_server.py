import requests

#-------------------------------------------------------------------------------------------------------
#test getting all members
print(requests.get("http://127.0.0.1:8000/").json())
#PASSED

#test getting members specified by ID
print(requests.get("http://127.0.0.1:8000/volunteers/0").json())
#PASSED

#test getting members specified by any information
#print(requests.get("http://127.0.0.1:8000/volunteers/?volunteer_id=0").json())
#FAILED


#-------------------------------------------------------------------------------------------------------
#test adding new member
print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={
            "volunteer_id": 1,
            "first_name": "Dante", 
            "last_name": "OConnell", 
            "email": "example", 
            "phone_number": 444, 
            "date_of_birth": "02192000",
            "address": "1 First Street, Origin, NY 00000",
            "skills": ["boring", "nerd", "skater"],
            "availability": ["Saturday", "Sunday"],
            "date_joined": "04012024",
            "background_check": True
        },
    ).json()
)
#print(requests.get("http://127.0.0.1:8000/").json())
#PASSED


#-------------------------------------------------------------------------------------------------------
#test updating a member specified by their ID
print(requests.put("http://127.0.0.1:8000/volunteers/0?first_name=Clara").json())
#print(requests.get("http://127.0.0.1:8000/").json())
#PASSED


#-------------------------------------------------------------------------------------------------------
#test deleting a member specified by their ID
print(requests.delete("http://127.0.0.1:8000/volunteers/1").json())
#print(requests.get("http://127.0.0.1:8000/").json())
#PASSED