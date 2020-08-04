import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from bson.objectid import ObjectId
from .helpers import login_required, before_request


notes = db.notes
users = db.users

@app.route('/')
@app.route('/index')
def index():
    if 'user_id' in session:
        userLoggedIn = True
        userid = session['user_id']
        user = users.find_one({'_id': userid})
        username = user['username']
        userNotes = notes.find({'author': username}).sort('_id', -1)
        userCategories = user['categories']
    else:
        userLoggedIn = False
        user = 'anonymous user'
        userNotes = []
        userCategories = []
    
    return render_template('index.html',
                           title='Home Page',
                           user=user,
                           userLoggedIn=userLoggedIn,
                           notes=userNotes,
                           categories=userCategories)

'''
Create a new note
'''
@app.route('/note/', methods=["GET", "POST"])
@login_required
def new_note():
    user = db.users.find_one(({"_id": session['user_id']}))
    note = {}
    username = user['username']
    userCategories = user['categories']
    return render_template('note.html',
                           note=note,
                           displayedTime=datetime.now().strftime('%m/%d/%Y'),
                           exists=False,
                           timestamp=datetime.now(),
                           user=user,
                           userLoggedIn=True,
                           categories=userCategories)

'''
Autosave the note
'''
@app.route('/autosave/', methods=["GET", "POST"])
@login_required
def autosave():
    user = db.users.find_one(({"_id": session['user_id']}))
    author = username = user['username']
    userCategories = user['categories']
    if request.method == 'POST':
        note = {}
        category = {}
        data = request.get_json('data')
        body = note['body'] = data['body']
        title = note['title'] = data['title']
        author = note['author'] = user['username']
        timestamp = note['timestamp'] = data['timestamp']
        category =categoryName = note['category'] = data['category']

    noteAlreadyExists = db.notes.find_one(
        {'$and': [{'timestamp': timestamp}, {'author': author}]})

    categoryAlreadyExists = db.users.find_one({'$and': [
        {"username": username},
        {"categories": category}
    ]
    })

    if not categoryAlreadyExists and len(categoryName)!=0:
        db.users.find_one_and_update(
            user, {'$push': {'categories': category}})

    if noteAlreadyExists:
        db.notes.update_one(noteAlreadyExists, {
                            '$set': {'body': body, 'title': title, 'category': category}})
    if not noteAlreadyExists:
        db.notes.insert(note)
        db.users.find_one_and_update(
            user, {'$push': {'notes': note['timestamp']}})
    # flask-to-return-nothing-but-only-run-script
    return('', 204)

'''
Save note through submitting the form
'''
@app.route('/page/', methods=["GET", "POST"])
@login_required
def page():
    user = db.users.find_one(({"_id": session['user_id']}))
    username = user['username']
    userCategories = user['categories']
    if request.method == 'POST':
        note = {}
        category = {}
        body = note['body'] = request.form['note_body']
        title = note['title'] = request.form['note_title']
        timestamp = request.form['note_timestamp']
        note['timestamp'] = timestamp
        categoryName = category['name'] = note['category'] = request.form['note_category']
        category['user'] = author = note['author'] = user['username']
        displayedTime = datetime.strptime(
            timestamp, '%Y-%m-%d %H:%M:%S.%f').strftime('%m/%d/%Y')
        alreadyExists = db.notes.find_one(
            {'$and': [{'timestamp': timestamp}, {'author': author}]})
        categoryAlreadyExists = db.users.find_one({'$and': [
            {"username": username},
            {"categories": categoryName}
        ]
        })
        if alreadyExists:
            db.notes.update_one(
                alreadyExists, {'$set': {'body': body, 'title': title, 'category': categoryName}})
        else:
            db.notes.insert(note)
            db.users.find_one_and_update(
                user, {'$push': {'notes': note['timestamp']}})
        if not categoryAlreadyExists and len(categoryName)!=0:
            db.users.find_one_and_update(
                user, {'$push': {'categories': categoryName}})
        flash("Note saved")
        #return('',204)
        #return render_template('note.html', note=note)
        return render_template('note.html',
                           note=note,
                           displayedTime=timestamp,
                           timestamp=timestamp,
                           user=user,
                           userLoggedIn=True,
                           categories=userCategories)

'''
View a previously created note in read-only mode
'''
@app.route('/read/<note_id>', methods=["GET", "POST"])
@login_required
def read(note_id):
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    user = db.users.find_one(
        {"_id": session['user_id']}
    )
    username = user['username']
    userCategories = user['categories']
    return render_template('read.html',
                           note=note,
                           user=db.users.find_one(
                               ({"_id": session['user_id']})),
                           timestamp=note['timestamp'],
                           displayedTime=datetime.strptime(
                               note['timestamp'], '%Y-%m-%d %H:%M:%S.%f').strftime('%m/%d/%Y'),
                           userLoggedIn=True,
                           exists=True,
                           categories=userCategories)


'''
View a previously created note in edit mode
'''
@app.route('/note/<note_id>', methods=["GET", "POST"])
@login_required
def note(note_id):
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    user = db.users.find_one(
        {"_id": session['user_id']}
    )
    username = user['username']
    userCategories = user['categories']
    return render_template('note.html',
                           note=note,
                           user=db.users.find_one(
                               ({"_id": session['user_id']})),
                           timestamp=note['timestamp'],
                           displayedTime=datetime.strptime(
                               note['timestamp'], '%Y-%m-%d %H:%M:%S.%f').strftime('%m/%d/%Y'),
                           userLoggedIn=True,
                           exists=True,
                           categories=userCategories)

'''
View notes according to category
'''
@app.route('/category/<cat>')
def category(cat):
    userid = session['user_id']
    user = users.find_one({'_id': userid})
    username = user['username']
    userCategories = user['categories']
    notes = db.notes.find(
        {'$and': [{'author': username}, {'category': cat}]})
    return render_template('index.html',
                           title='Home Page',
                           user=user,
                           userLoggedIn=True,
                           notes=notes,
                           categories=userCategories,
                           currentCat=cat)

'''
Delete categories
'''
@app.route('/delete_category/<cat>')
def delete_category(cat):
    userid = session['user_id']
    user = users.find_one({'_id': userid})
    username = user['username']
    userCategories = user['categories']
    db.notes.update(
        {'$and': [{'author': username}, {'category': cat}]},
        {'$unset': {"category": ""}}
    )
    db.users.update(
        {"_id": session['user_id']},
        {'$pull': {"categories": {'$in': [cat]}}}
    )
    print('end')
    return redirect(url_for('index'))

'''
Delete note
'''
@app.route('/delete_note/<note_id>')
def delete_note(note_id):
    notes = db.notes
    notes.remove({'_id': ObjectId(note_id)})
    return redirect(url_for('index'))


@app.route('/notLoggedIn/', methods=["GET", "POST"])
def notLoggedIn():
    return render_template('notLoggedIn.html')


'''
Search notes
'''
@app.route('/search', methods=["GET", "POST"])
@login_required
def search():
    # loggedIn = False

    if 'user_id' in session:
        userLoggedIn = True
        user = db.users.find_one(({"_id": session['user_id']}))
        author = user['username']
        user_notes = user['notes']

    user_notes = []

    if request.method == "POST":
        searchTerm = request.form.get('searchTerm')
        if userLoggedIn == True:
            user_notes = db.notes.aggregate([
                {'$match': {'$text': {'$search': searchTerm}}},
                {'$match': {'author': author}}
            ])
        public_notes = db.notes.aggregate([
            {'$match': {'$text': {'$search': searchTerm}}},
            {'$match': {'public': 'True'}}
        ])

        '''
        https://stackoverflow.com/questions/31954014/typeerror-commandcursor-object-has-no-attribute-getitem
        In PyMongo 3 the aggregate method returns an iterable of result documents (an instance of CommandCursor), not a single document. 
        You have to iterate the results, or alternatively turn them into a list with list(res).
        '''

        return render_template('search_results.html',
                               user=user,
                               user_notes=user_notes,
                               public_notes=public_notes,
                               userLoggedIn=True)
    # GET route
    else:
        return render_template('search.html',
                               userLoggedIn=True,
                               user=user)


'''
Register
'''
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        users = db.users
        form = request.form.to_dict()
        alreadyExists = users.find_one({"username": form['username']})
        if alreadyExists:
            flash("Username already exists!")
            return render_template('register.html')

        if form['confirmation'] != form['password']:
            flash("Passwords do not match")
            return render_template('register.html')

        del form['confirmation']
        form['password'] = generate_password_hash(form['password'])

        form['categories'] = ["Home", "Work"]

        if not alreadyExists:
            users.insert_one(form)

        # log user in
        user = db.users.find_one({"username": form['username']})

        # Remember which user has logged in
        session['user_id'] = user['_id']
        session['username'] = user['username']

        # Redirect user to home page
        flash("Congratulations, you are now a registered user!")
        return redirect('/')

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

'''
Login
Code for login from CS50 Finance
https://cs50.harvard.edu/x/2020/tracks/web/finance/
'''
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        users = db.users
        loginform = request.form.to_dict()
        user = users.find_one({"username": loginform['username']})
        if not user:
            '''flash only happens click another href'''
            flash('Invalid username')
            return render_template('login.html')
        elif not check_password_hash(user['password'], loginform['password']):
            flash('Invalid password')
            return render_template('login.html')
        else:
            session['user_id'] = user['_id']
            session['username'] = user['username']
            userLoggedIn = True
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

'''
Logout
Code for logout from CS50 Finance
https://cs50.harvard.edu/x/2020/tracks/web/finance/
'''
@app.route('/logout')
def logout():
    session.clear()
    userLoggedIn = False
    return redirect(url_for('index'))

'''
User profile
'''
@app.route('/user/<username>')
@login_required
def user(username):
    if 'user_id' in session:
        users = db.users
        userid = session['user_id']
        user = users.find_one({'_id': userid})
        uname = user['username']
        numberOfNotes = len(user['notes'])
        return render_template('user.html',
                               title='Profile page',
                               user=user,
                               username=uname,
                               userLoggedIn=True,
                               numberOfNotes=numberOfNotes)
    else:
        return render_template('index.html',
                               user='anonymous user')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
