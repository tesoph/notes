from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from app import app, db
# from app.forms import LoginForm
from flask_pymongo import PyMongo
#from flask_mongoengine import MongoEngine
import os
# from app.models import User
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sys
from app.wiki import get_content
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
    #userLoggedIn = True if 'user_id' in session else False
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
    if 'user_id' in session:
         users=db.users
         userid=session['user_id']
         user = users.find_one({'_id': userid})
         return render_template('index.html', title='Home Page', user=user, userLoggedIn=True)
    else:
        return render_template('index.html', title='Home Page', user='anonymous user', userLoggedIn=False)
# ...'

# ...


@app.route('/logout')
def logout():

    '''
    #flask-login
    #logout_user()
    '''
    session.clear()
    userLoggedIn=False
    return redirect(url_for('index'))


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    flask-login
    if current_user.is_authenticated:
        flash("Already logged in! Log out to login in as a different user")
        return redirect(url_for('index'))
    '''
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        users=db.users
        loginform = request.form.to_dict()
        user = users.find_one({"username": loginform['username']})
        if not user or not check_password_hash(user['password'], loginform['password']):
            flash('Invalid username or password')
            return render_template('login.html')
        else:
            session['user_id'] = user['_id']
            session['username']=user['username']
            userLoggedIn=True 
            return redirect("/")
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
        '''
        flask-login
        if not User.check_password((user['password']), (loginform['password'])):
            flash("Invalid username or password")
            return render_template('login.html')
            #return redirect('/login')
        '''
        '''
        flask-login
        user_obj = User(username=loginform['username'])
        login_user(user_obj)
        '''
        # Ensure username exists and password is correct
        '''
        # Remember which user has logged in
        # session['user_id'] = (db.users.find_one({"username": user['username']}))['_id']
        '''
        # Redirect user to home page
        

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
        users=db.users
        form = request.form.to_dict()
        alreadyExists = users.find_one({"username": form['username']})
        if alreadyExists:
            flash("Username already exists!")
            return render_template('register.html')
        
        del form['confirmation']
        #plain = form["password"]
        form['password'] = generate_password_hash(form['password'])

   
        #raise ValueError('Username already exists, choose a different username')
        # display flashed message
        if not alreadyExists:
            users.insert_one(form)

        # log user in
        user=db.users.find_one({"username": form['username']})
        # Remember which user has logged in
        # session["user_id"] = rows[0]["id"]
        session['user_id'] = user['_id']
        session['username'] = user['username']

        # Redirect user to home page
        flash("Congratulations, you are now a registered user!")

        '''
        #flask-login
        user_obj = User(username=form['username'])
        login_user(user_obj)
        '''
        

        return render_template('index.html', user =user)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        flash("registering")
        return render_template("register.html")

'''
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
@app.route('/user/<username>')
# @login_required
def user(username):
    if 'user_id' in session:
         users=db.users
         userid=session['user_id']
         user = users.find_one({'_id': userid})
         return render_template('user.html', title='Profile page', user=user, username=user['username'])
    else:
        return render_template('index.html', user='anonymous user')
    #user_obj = User(username)
    #u = db.users.find_one({"_id": session['user_id']})
    #u = current_user
    #user_obj =User(current_user)
    # user = User.query.filter_by(username=username).first_or_404()
    '''
    posts = [
            {'author': u, 'body': 'Test post #1'},
            {'author': u, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=u, posts=posts)
    '''

@app.before_request
def before_request():
    time= datetime.now()
    if 'user_id' in session:
            # db.users.find_one_and_update({"_id": session['user_id']}, {'$set': {"last_seen": 'now'}})
            db.users.update_one({"_id": session['user_id']}, {'$set': {"last_seen": time}})
            #user =db.users.find_one({"_id": session['user_id']})
            #time = user['last_seen']
            #print(f'updated? {time}', file=sys.stderr)
    '''
    if current_user.is_authenticated:
        t=datetime.now()
        u=current_user
    '''
        #current_user['last_seen'] = datetime.now()
        #user =db.users.find_one({"_id": current_user._id})
        #db.users.update_one(user, {'$set': {"last_seen": t}})
        #u.set_lastseen(t)
        #db.session.commit()
        #u = current_user


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

@app.route('/search', methods=["GET", "POST"])
def search():
    #POST route
    if request.method == "POST":
        searchTerm = request.form.get('searchTerm')
        pageContent=get_content(searchTerm)
        #render list
        return render_template('wiki.html', content=pageContent)
    #GET route
    else:
         return render_template('search.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
