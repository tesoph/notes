from app import db
from flask_mongoengine import MongoEngine

class User(db.Document):
    first_name = db.StringField(max_length=50)
