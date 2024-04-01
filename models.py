from sqlalchemy import String, Boolean, Integer, Column, TIMESTAMP
from .database import Base

# initialize the table
class Product(Base):
    __tablename__ = 'volunteers'
    
    volunteer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    date_of_birth = Column(TIMESTAMP(timezone=True))
    address = Column(String)
    skills = Column(String)
    availability = Column(String)
    date_joined = Column(TIMESTAMP(timezone=True))
    background_check = Column(Boolean)
