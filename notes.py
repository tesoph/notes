import os
from app import app, db
# models
notes = db.notes
categories = db.categories
users = db.users
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
