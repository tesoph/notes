from flask import Flask
from config import Config
from flask_pymongo import PyMongo
import os 
from flask_mongoengine import MongoEngine
#Creates the app object as an instance of class Flask
#__name__is a Python predefined variable which is set to the name of the module in which it is used.
app = Flask(__name__)
#'config' = config.py, Config is actual class
app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)
db = MongoEngine(app)
#routes module is imported at the bottom.
#Workaround to circular imports
#(routes needs to import app which is defined above)
from app import routes
#from app import routes, models