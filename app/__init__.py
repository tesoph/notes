from flask import Flask
from config import Config

#Creates the app object as an instance of class Flask
#__name__is a Python predefined variable which is set to the name of the module in which it is used.
app = Flask(__name__)
#'config' = config.py, Config is actual class
app.config.from_object(Config)

#routes module is imported at the bottom.
#Workaround to circular imports
#(routes needs to import app which is defined above)
from app import routes