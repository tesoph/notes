import os
from tempfile import mkdtemp

basedir = os.path.abspath(os.path.dirname(__file__))
##'sqlite:///' + os.path.join(basedir, 'app.db')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI=os.environ['MONGO_URI'] or \
        os.path.join(basedir, 'app.json')
    MONGO_DBNAME=os.environ['MONGO_DBNAME']
    MONGODB_SETTINGS = {
    'db': 'microblog',
    'host': os.environ['MONGO_URI']
    }
    SESSION_FILE_DIR = mkdtemp()
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"