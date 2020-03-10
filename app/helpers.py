from app import app, db
from functools import wraps
from flask import redirect, session
from datetime import datetime

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.before_request
def before_request():
    time = datetime.now()
    if 'user_id' in session:
        db.users.update_one({"_id": session['user_id']}, {
                            '$set': {"last_seen": time}})
