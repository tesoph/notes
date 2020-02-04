from app import db, login
from flask_mongoengine import MongoEngine
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
# chp5 user-logins
#from flask_login import UserMixin
from flask_login import current_user, login_user, logout_user, login_required

'''
db.document=


AttributeError: 'str' object has no attribute 'codec_options'
      super(Collection, self).__init__(

            codec_options or database.codec_options,

            
class User(db.Document):
    first_name = db.StringField(max_length=50)
'''
# class User(Document):


class User(Document):
    # user = db.users.find_one({"username": u['username']})
    # class User(UserMixin, Document)
    # class User(db.UserMixin, db.Document)
    ##username = StringField(max_length=50)
    # hash
    #last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    #last_seen = DateTimeField(default=datetime.datetime.now)
    #password = db.users.find_one
    #def __init__(self, username, password_hash):
    def __init__(self, username):
        user = db.users.find_one({"username": username})
        self.username =username
        self.password = user['password']
        self._id= user['_id']
       
        #self.password_hash = Document['password']
        #self.password=password

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    '''
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)'''
        
    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return self.username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

@login.user_loader
def load_user(username):
    u = db.users.find_one({'username': username})
    #return u
    return User(u['username'])


'''
don't use flask-login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
'''
# @login.user_loader
# def load_user(id):
# return User.query.get(int(id))

'''
class Article(Document):
    body = StringField(max_lenth=100)
    user = ReferenceField(User)
'''
