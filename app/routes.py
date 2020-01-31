from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.forms import LoginForm
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import os 
from app.models import User
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import current_user, login_user
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
   #return render_template('index.html', title='Home', user=u)
    return render_template("index.html", title='Home Page',user=u)
# ...

# ...

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    '''
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)