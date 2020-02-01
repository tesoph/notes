from flask import Flask
from config import Config
from flask_pymongo import PyMongo
import os 
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
#from flask_login import LoginManager
#from flask_login import current_user, login_user, logout_user, login_required
from flask_session import Session

#Creates the app object as an instance of class Flask
#__name__is a Python predefined variable which is set to the name of the module in which it is used.
app = Flask(__name__)
#'config' = config.py, Config is actual class
app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)
#db = MongoEngine(app)
client = MongoClient(Config.MONGO_URI)
db = client.microblog

Session(app)
#login-manager
'''
login= LoginManager(app)
login.login_view = 'login'
'''


#routes module is imported at the bottom.
#Workaround to circular imports
#(routes needs to import app which is defined above)
from app import routes
#from app import routes, models