from app import app, db
from functools import wraps
from flask import redirect, session
from datetime import datetime

"""
Decorate routes to require login.
From: https://cs50.harvard.edu/x/2020/tracks/web/finance/
http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
"""
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

"""
Recording The Last Visit Time For a User 
From:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars
"""
@app.before_request
def before_request():
    time = datetime.now()
    if 'user_id' in session:
        db.users.update_one({"_id": session['user_id']}, {
                            '$set': {"last_seen": time}})
