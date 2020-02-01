from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from app import app
from app import db
#from app.forms import LoginForm
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import os
#from app.models import User
#from flask_login import current_user, login_user
#from app.models import User
#from flask_login import logout_user
#from flask_login import current_user, login_user
#from app.models import User
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

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
    # u=db.users.count()
    # "username": user['username'
    '''
    id = session['user_id']
    u=db.users.find_one({"_id": id})
    name = u['username']
    '''
    # db.users.find_one({"username": user['username']}))[id]
    #u =mongo.db.users.count()
    # u='ray'
    #  name='emma'
    '''
    if session:
        userid=session["user_id"]
        user = db.users.find_one({"_id": session['user_id']})
        name = user['name]']
    #return render_template('index.html', title='Home', user=u)
        return render_template("index.html", title='Home Page', user=user, name=name)
    else:
        return render_template("index.html", title='Home Page')
        '''
    if session:
        userid = session['user_id']
        u = db.users.find_one({"_id": userid})
        name = u['username']
        return render_template("index.html", title='Home Page', user=name)
    else:
        return render_template("index.html", title='Home Page', user='unsigned in user')
# ...'

# ...


@app.route('/logout')
def logout():
    # logout_user()
    session.clear()
    return redirect(url_for('index'))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        userinfo = request.form.to_dict()
        #user = db.users.find_one({"username": user['username']})
        user = db.users.find_one({"username": userinfo['username']})
        # Ensure username exists and password is correct

        # Remember which user has logged in
        session['user_id'] = (db.users.find_one(
            {"username": user['username']}))['_id']
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        '''
        # check password confirmation
        if not request.form.get('password') == request.form.get('confirmation'):
            return apology("passwords don't match", 403)
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        '''

        user = request.form.to_dict()
        alreadyExists = db.users.find_one({"username": user['username']})

        del user['confirmation']
        plain = request.form.get("password")
        user['password'] = generate_password_hash(plain)

        if alreadyExists:
            raise ValueError(
                'Username already exists, choose a different username')
        # display flashed message
        if not alreadyExists:
            db.users.insert_one(user)

        # log user in
        #user=db.users.find_one({"username": user['username']})
        # Remember which user has logged in
        #session["user_id"] = rows[0]["id"]
        session['user_id'] = (db.users.find_one(
            {"username": user['username']}))['_id']
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route('/user')
# @login_required
def user():
    if session:
        u = db.users.find_one({"_id": session['user_id']})
    #user = User.query.filter_by(username=username).first_or_404()
        posts = [
            {'author': user, 'body': 'Test post #1'},
            {'author': user, 'body': 'Test post #2'}
        ]
        return render_template('user.html', user=u, posts=posts)
    else:
        return redirect('/login')
