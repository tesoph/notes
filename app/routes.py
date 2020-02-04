from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from app import app
from app import db
# from app.forms import LoginForm
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import os
# from app.models import User
# from flask_login import current_user, login_user
from app.models import User
# from flask_login import logout_user
from flask_login import current_user, login_user, logout_user
# from app.models import User
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sys

# mongo = PyMongo(app)

'''
app.config['MONGODB_SETTINGS'] = {
    'db': 'microblog',
    'host': os.environ['MONGO_URI']
}'''
# db = MongoEngine(app)
'''
A decorator modifies the function that follows it.
@app.route('/index') = when web browser requests the /index url,
Flask invokes this function and passes the return value back to the browser as a response
'''
@app.route('/')
@app.route('/index')
def index():
    flash("hello")
    # u=db.users.count()
    # "username": user['username'
    '''
    id = session['user_id']
    u=db.users.find_one({"_id": id})
    name = u['username']
    '''
    # db.users.find_one({"username": user['username']}))[id]
    # u =mongo.db.users.count()
    # u='ray'
    #  name='emma'
    '''
    if session:
        userid=session["user_id"]
        user = db.users.find_one({"_id": session['user_id']})
        name = user['name]']
    # return render_template('index.html', title='Home', user=u)
        return render_template("index.html", title='Home Page', user=user, name=name)
    else:
        return render_template("index.html", title='Home Page')
        '''
    '''
    if session:
        userid = session['user_id']
        u = db.users.find_one({"_id": userid})
        name = u['username']
        return render_template("index.html", title='Home Page', user=name)
    else:
        return render_template("index.html", title='Home Page', user='unsigned in user')
    '''
    return render_template('index.html', title='Home Page')
# ...'

# ...


@app.route('/logout')
def logout():
    logout_user()
    #session.clear()
    return redirect(url_for('index'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Already logged in! Log out to login in as a different user")
        return redirect(url_for('index'))
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        u = request.form.to_dict()
        user = db.users.find_one({"username": u['username']})
        #user= db.users.find_one({"username": u['username']})
        #user = User.query.filter_by(username=u['username']).first()
        '''
        user_obj = User(username=u['username'])
        if user_obj.check_password(u['password']):
            flash("Invalid password")
            return redirect(url_for('login'))'''
        #https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb
        #?requires page load to display flash msgs?
        #https://stackoverflow.com/questions/58521122/no-message-flashing-on-flask-without-error-message
        if not User.check_password((user['password']), (u['password'])):
            flash("Invalid username or password")
            return render_template('login.html')
            #return redirect('/login')
        user_obj = User(username=u['username'])
        login_user(user_obj)
        # Ensure username exists and password is correct
        '''
        # Remember which user has logged in
        # session['user_id'] = (db.users.find_one({"username": user['username']}))['_id']
        '''
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

        u = request.form.to_dict()
        alreadyExists = db.users.find_one({"username": u['username']})

        del u['confirmation']
        plain = request.form.get("password")
        u['password'] = generate_password_hash(plain)

        if alreadyExists:
            flash("Username already exists!")
            return render_template('register.html')
            #raise ValueError('Username already exists, choose a different username')
        # display flashed message
        if not alreadyExists:
            db.users.insert_one(u)

        # log user in
        # user=db.users.find_one({"username": user['username']})
        # Remember which user has logged in
        # session["user_id"] = rows[0]["id"]
        session['user_id'] = (db.users.find_one(
            {"username": u['username']}))['_id']
        # Redirect user to home page
        flash("Congratulations, you are now a registered user!")
        user_obj = User(username=u['username'])
        login_user(user_obj)
        return render_template('index.html')

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        flash("registering")
        return render_template("register.html")


@app.route('/user')
# @login_required
def user():
    if session:
        u = db.users.find_one({"_id": session['user_id']})
    # user = User.query.filter_by(username=username).first_or_404()
        posts = [
            {'author': user, 'body': 'Test post #1'},
            {'author': user, 'body': 'Test post #2'}
        ]
        return render_template('user.html', user=u, posts=posts)
    else:
        return redirect('/login')

'''
@app.before_request
def before_request():
    
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        
    t= datetime.now()
    print(f'hi, {t}', file=sys.stderr)
    if session:
            # db.users.find_one_and_update({"_id": session['user_id']}, {'$set': {"last_seen": 'now'}})
            db.users.update_one({"_id": session['user_id']}, {'$set': {"last_seen": t}})
            user =db.users.find_one({"_id": session['user_id']})
            time = user['last_seen']
            print(f'updated? {time}', file=sys.stderr)
'''
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
