from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.forms import LoginForm
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import os 
from app.models import User


#mongo = PyMongo(app)

'''
app.config['MONGODB_SETTINGS'] = {
    'db': 'microblog',
    'host': os.environ['MONGO_URI']
}'''
#db = MongoEngine(app)
'''
A decorator modifies the function that follows it.
@app.route('/index') = when web browser requests the /index url,
Flask invokes this function and passes the return value back to the browser as a response
'''
@app.route('/')
@app.route('/index')
def index():
    u=db.users.count()
    #u =mongo.db.users.count()
    return render_template('index.html', title='Home', user=u)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)