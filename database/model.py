from .db import db 

class Bus(db.Document):
    number_plate  =  db.StringField(required=True, unique=True)
    manufacturer = db.StringField(required=True)
    model = db.StringField(required=True)
    year = db.IntField(required=True)
    capacity =  db.IntField(required=True)
    
