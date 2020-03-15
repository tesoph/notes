from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, json
from app import app, db
# from app.forms import LoginForm
from flask_pymongo import PyMongo
# from flask_mongoengine import MongoEngine
import os
# from app.models import User
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sys
from app.wiki import get_content, get_title
# for login_required
from functools import wraps
# logi_required fom cs50
# whats args and kwargs
# mongo = PyMongo(app)
# from app.forms import loginForm
# import requests
import urllib
import json
import requests
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
from urllib.parse import urlparse
from app.forms import NoteForm
from .helpers import login_required, before_request




@app.route('/')
@app.route('/index')
def index():
    #note = db.notes.find_one(
    #        {'$and': [{'url': url}, {'author': user['username']}]})
    notes = db.notes
    #Get the 10 most recent 'public' notes 
    #-1 means sorted from newest to oldest
    recentNotes = notes.find({"public": "True"}).limit(10).sort([('_id', -1)])

    if 'user_id' in session:
        users = db.users
        userid = session['user_id']
        user = users.find_one({'_id': userid})
        author = user['username']
        userNotes = notes.find({'author': author})
        return render_template('index.html',
                               title='Home Page',
                               user=user,
                               userLoggedIn=True,
                               notes=userNotes,
                               recentNotes=recentNotes)
    # if no user is logged in call them anonymous user
    return render_template('index.html',
                           title='Home Page',
                           user='anonymous user',
                           userLoggedIn=False,
                           recentNotes=recentNotes,
                           )


'''
Bookmarklet #1
Clicking the bookmarklet returns the wiki page in an iframe on the app site
'''
"""
@app.route('/page/', methods=["GET", "POST"])
@login_required
def page():

    user = db.users.find_one(({"_id": session['user_id']}))
    #Database is searched for a note by the logged in user from the same wikipedia page
    if request.method == "GET":
        url = request.args.get('url')
        title = request.args.get('title')
        note = db.notes.find_one(
            {'$and': [{'url': url}, {'author': user['username']}]})
        #If the note exists already it is returned to the user on the note taking page
        if note:
            public = note['public']
            public = str(public)
            print('note exists, is it public or private?' + str(public))
            return render_template('page.html',
                                   url=url,
                                   note=note,
                                   title=title,
                                   public=public)
        #Else if the note does not exist, the note is automatically set to private and the notetaking page is returned
        else:
            public = False
            public = str(public)
            return render_template('page.html',
                                   url=url,
                                   title=title,
                                   public=public)

    if request.method == 'POST':

        # https://stackoverflow.com/questions/25491090/how-to-use-python-to-execute-a-curl-command
        # https://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url/13921930#13921930
        url = request.values.get('url')
        response = requests.post(url)
        resp = response.text
        html_doc = resp
        soup = BeautifulSoup(html_doc, 'html.parser')
        print('soup title:' + soup.title.string)

        note = {}
        note['url'] = request.values.get('url')
        body = note['body'] = request.form['note']
        title = note['title'] = request.form['note_title']
        public = note['public'] = request.form['publicOption']
        public = str(public)
        author = note['author'] = user['username']

        # https://docs.mongodb.com/manual/reference/operator/query/and/
        # db.inventory.find( { $and: [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } )
        # db_request.append({'$and': [{'indoor': True}, {'outdoor': True}]})
        alreadyExists = db.notes.find_one(
            {'$and': [{'url': url}, {'author': author}]})
        if not alreadyExists:
            db.notes.insert(note)
            db.users.find_one_and_update(
                user, {'$push': {'notes': note['url']}})
            return render_template('page.html',
                                   url=url,
                                   note=note,
                                   public=public)
        else:
            # unhashable type 'dict'
            db.notes.update_one(
                alreadyExists, {'$set': {'body': body, 'public': public}})
            public = str(public)
            return render_template('page.html',
                                   url=url,
                                   note=note,
                                   public=public)
"""

'''
Bookmarklet #1
Clicking the bookmarklet returns the wiki page in an iframe on the app site
'''
@app.route('/page/', methods=["GET", "POST"])
@login_required
def page():

    user = db.users.find_one(({"_id": session['user_id']}))
    #Database is searched for a note by the logged in user from the same wikipedia page
    if request.method == "GET":
        url = request.args.get('url')
        title = request.args.get('title')
        note = db.notes.find_one(
            {'$and': [{'url': url}, {'author': user['username']}]})
        #If the note exists already it is returned to the user on the note taking page
        if note:
            public = note['public']
            public = str(public)
            print('note exists, is it public or private?' + str(public))
        if not note:
            note = {}
            public=False
        #Else if the note does not exist, the note is automatically set to private and the notetaking page is returned
    
        return render_template('page.html',
                                   url=url,
                                   note=note,
                                   title=title,
                                   public=public)

    if request.method == 'POST':

        # https://stackoverflow.com/questions/25491090/how-to-use-python-to-execute-a-curl-command
        # https://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url/13921930#13921930
        url = request.values.get('url')
        response = requests.post(url)
        resp = response.text
        html_doc = resp
        soup = BeautifulSoup(html_doc, 'html.parser')
        print('soup title:' + soup.title.string)

        note = {}
        note['url'] = request.values.get('url')
        body = note['body'] = request.form['note']
        title = note['title'] = request.form['note_title']
        public = note['public'] = request.form['publicOption']
        public = str(public)
        author = note['author'] = user['username']

        # https://docs.mongodb.com/manual/reference/operator/query/and/
        # db.inventory.find( { $and: [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } )
        # db_request.append({'$and': [{'indoor': True}, {'outdoor': True}]})
        alreadyExists = db.notes.find_one(
            {'$and': [{'url': url}, {'author': author}]})
        if not alreadyExists:
            db.notes.insert(note)
            db.users.find_one_and_update(
                user, {'$push': {'notes': note['url']}})
            return render_template('page.html',
                                   url=url,
                                   note=note,
                                   public=public,
                                   title=title)
        else:
            # unhashable type 'dict'
            db.notes.update_one(
                alreadyExists, {'$set': {'body': body, 'public': public}})
            public = str(public)
            return render_template('page.html',
                                   url=url,
                                   note=note,
                                   public=public)

'''
Delete note
'''
@app.route('/delete_note/<note_id>')
def delete_note(note_id):
    notes = db.notes
    notes.remove({'_id': ObjectId(note_id)})
    return redirect(url_for('index'))


''''
Edit note #1
from code institue task manager app
https://github.com/Code-Institute-Solutions/TaskManager/blob/master/04-EditingATask/05-update_the_task_in_the_database/app.py
'''
@app.route('/edit_note_title/<note_id>')
def edit_note_title(note_id):
    notes = db.notes
    note = notes.find_one({'_id': ObjectId(note_id)})
    return render_template('edit_note.html',
                           note=note)

'''
Edit note #2
'''
@app.route('/update_task/<note_id>', methods=["POST"])
def update_note(note_id):
    notes = db.notes
    note = notes.find_one({'_id': ObjectId(note_id)})
    notes.update_one(note,
                     {'$set': {
                         'title': request.form.get('note_title'),
                         'body': request.form.get('note')
                     }
                     })
    return redirect(url_for('index'))


'''
Clicking a note on the index page
'''
@app.route('/note/<note_id>', methods=["GET", "POST"])
@login_required
def note(note_id):
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    url = note['url']
    '''
    #https://stackoverflow.com/questions/12030487/mongo-conditional-for-key-doesnt-exist
    cursor =note.find({'public': { '$exists': True }})
    '''
    # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
    if 'public' in note:
        public = note['public']
    else:
        public = False
    public = str(public)
    user = db.users.find_one(({"_id": session['user_id']}))
    return render_template('page.html',
                           url=url,
                           note=note,
                           public=public)

"""
'''
Clicking a note on the index page
'''
@app.route('/note_view/<note_id>', methods=["GET", "POST"])
#@login_required
def note(note_id):
    note = db.notes.find_one({'_id': ObjectId(note_id)})
    url = note['url']
    '''
    #https://stackoverflow.com/questions/12030487/mongo-conditional-for-key-doesnt-exist
    cursor =note.find({'public': { '$exists': True }})
    '''
    # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
    if 'public' in note:
        public = note['public']
    else:
        public = False
    public = str(public)
    user = db.users.find_one(({"_id": session['user_id']}))
    return render_template('page.html',
                           url=url,
                           note=note,
                           public=public)
"""

@app.route('/notLoggedIn/', methods=["GET", "POST"])
def notLoggedIn():
   
    return render_template('notLoggedIn.html')
'''
Search notes
'''
@app.route('/search_notes', methods=["GET", "POST"])
# @login_required
def search_notes():
    loggedIn = False

    if 'user_id' in session:
        loggedIn = True
        user = db.users.find_one(({"_id": session['user_id']}))
        author = user['username']
        user_notes = user['notes']

    all_notes = []
    user_notes = []

    if request.method == "POST":
        searchTerm = request.form.get('searchTerm')
        if loggedIn == True:
            user_notes = db.notes.aggregate([
                {'$match': {'$text': {'$search': searchTerm}}},
                {'$match': {'author': author}}
            ])
        public_notes = db.notes.aggregate([
            {'$match': {'$text': {'$search': searchTerm}}},
            {'$match': {'public': 'True'}}
        ])

        # https://stackoverflow.com/questions/31954014/typeerror-commandcursor-object-has-no-attribute-getitem
        '''
        In PyMongo 3 the aggregate method returns an iterable of result documents (an instance of CommandCursor), not a single document. 
        You have to iterate the results, or alternatively turn them into a list with list(res).
        '''

        return render_template('notes.html',
                               user_notes=user_notes,
                               public_notes=public_notes,
                               loggedIn=loggedIn)
    # GET route
    else:
        return render_template('search_notes.html')


@app.route('/logout')
def logout():
    '''
    # flask-login
    # logout_user()
    '''
    session.clear()
    userLoggedIn = False
    return redirect(url_for('index'))


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

        if not alreadyExists:
            users.insert_one(form)

        # log user in
        user = db.users.find_one({"username": form['username']})

        # Remember which user has logged in
        session['user_id'] = user['_id']
        session['username'] = user['username']

        # Redirect user to home page
        flash("Congratulations, you are now a registered user!")
        return render_template('index.html', user=user)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route('/user/<username>')
@login_required
def user(username):
    if 'user_id' in session:
        users = db.users
        userid = session['user_id']
        user = users.find_one({'_id': userid})
        uname = user['username']
        return render_template('user.html',
                               title='Profile page',
                               user=user,
                               username=uname)
    else:
        return render_template('index.html',
                               user='anonymous user')




'''
Route for bookmarklet to save page url to list (no notes)
'''
@app.route('/add/', methods=["GET", "POST"])
@login_required
def add():
    url = request.args.get('url')
    response = requests.post(url)
    resp = response.text
    html_doc = resp
    soup = BeautifulSoup(html_doc, 'html.parser')
    print('soup title:' + soup.title.string)
    page = {}
    page['url'] = request.args.get('url')
    page['title'] = soup.title.string
    print(page)
    db.users.find_one_and_update({"_id": session['user_id']}, {
                                 "$push": {"saved_pages": page}})
    # https://charlesleifer.com/blog/building-bookmarking-service-python-and-phantomjs/
    '''
    password = request.args.get('password')
    if password != PASSWORD:
        abort(404)
    '''
    url = request.args.get('url')
    return redirect(url)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
