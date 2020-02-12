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
#for login_required
from functools import wraps
#logi_required fom cs50
#whats args and kwargs
# mongo = PyMongo(app)
from app.forms import loginForm
'''
JQMIGRATE: Migrate is installed with logging active, version 3.1.0
'''
'''
 * Debugger PIN: 244-756-859
127.0.0.1 - - [11/Feb/2020 22:16:50] code 400, message Bad HTTP/0.9 request type ('\x16\x03\x01\x02\x00\x01\x00\x01ü\x03\x03\x1bÆ\x15FWïÊ9«:Mn©^\x84ÈL¼\x10`ÔÆ\x9d§wï\x8f~t\x88tØ')
127.0.0.1 - - [11/Feb/2020 22:16:50] "üFWïÊ9«:Mn©^
                                                  ÈL¼`ÔÆ~ttØ ËØ²ãß7WÝ¼"¥f¥
                                                                          dVèû~üØ¼C(¼
                                                                                     Y%"À+À/À,À0Ì©Ì¨ÀÀlB
µÝó^ûÊ DVä$Æ»ÅEË©lP é¥3IÊÛÕTÑäP
                               [×E µÆ"À+À/À,À0Ì©Ì¨ÀÀÄÓë
                                                       3=ÍP}:Håõ± 2ÅZÌ
¡á³r_[,lâµàCq9w" HTTPStatus.BAD_REQUEST -
27.0.0.1 - - [11/Feb/2020 22:17:34] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Feb/2020 22:17:45] code 400, message Bad request version (']¹1|\x8d\x9b7Ö\x10Ä\x82\x1bF\x00"\x1a\x1a\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x00')
127.0.0.1 - - [11/Feb/2020 22:17:45] "ü;Iü\S½q­wÒIÜ9ÅÕvwgX5°Ù´'ð á      H<¡Ó®sùÄ"À+À/À,À0Ì©Ì¨ÀÀ>Æ±ÒÎ7Tè
<þäe²n<ù¿©¨yd®<jâeÃUX"::À+À/À,À0Ì©Ì¨ÀÀeL£ÉÊÆô§f¹ÿ¿v
Á å6Ô§þ3æ³      E¦ÏVkI¡­åü"ÚÚÀ+À/À,À0Ì©Ì¨ÀÀò<   a}
                                                  RÐoz Z" HTTPStatus.BAD_REQUEST -
127.0.0.1 - - [11/Feb/2020 22:17:46] code 400, message Bad request version ('ñ\x11s½!hòqµ.±éeK±hûß¡H\x94õözQ\x00"ªª\x13\x01\x13\x02\x13\x03À+À/À,À0Ì©Ì¨À\x13À\x14\x00\x9c\x00\x9d\x00/\x005\x00')
127.0.0.1 - - [11/Feb/2020 22:17:46] "ü¬ø¾ ³ó;n¬]½âæ?QçÈJîég/×Sù £Öfr
ñs½!hòqµ.±éeK±hûß¡HõözQ"ªªÀ+À/À,À0Ì©Ì¨ÀÀÕr|áé!M]Cg¶·´·×
'''
'''
*whats g

This example assumes that the login page is called 'login' and that the current user is stored in g.user and is None if there is no-one logged in.
'''
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
    #latest saved articles
    if 'user_id' in session:
         users=db.users
         userid=session['user_id']
         user = users.find_one({'_id': userid})
         #pages = user['saved_pages']
         #articles = db.articles
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
    """Log user in"""
    
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        users=db.users
        loginform = request.form.to_dict()
        user = users.find_one({"username": loginform['username']})
        if not user or not check_password_hash(user['password'], loginform['password']):
            '''flash only happens click another href'''
            flash('Invalid username or password')
            return render_template('login.html')
        else:
            session['user_id'] = user['_id']
            session['username']=user['username']
            userLoggedIn=True 
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
        users=db.users
        form = request.form.to_dict()
        alreadyExists = users.find_one({"username": form['username']})
        if alreadyExists:
            flash("Username already exists!")
            return render_template('register.html')
        if form['confirmation'] != form['password']:
            flash("Passwords do not match")
            return render_template('register.html')
        
        del form['confirmation']
        if not alreadyExists:
            users.insert_one(form)

        # log user in
        user=db.users.find_one({"username": form['username']})

        # Remember which user has logged in
        session['user_id'] = user['_id']
        session['username'] = user['username']

        # Redirect user to home page
        flash("Congratulations, you are now a registered user!")
        return render_template('index.html', user =user)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
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
         uname=user['username']
         return render_template('user.html', title='Profile page', user=user, username=uname)
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
        pageContent=[]
        searchTerm = request.form.get('searchTerm')
        pageContent=get_content(searchTerm)
        #render list
        return render_template('wiki.html', content=pageContent)
    #GET route
    else:
         return render_template('search.html')
'''
class Bookmark(db.Model):
    url = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
    image = CharField(default='')
    javascript:location.href='http://127.0.0.1:5000/add/?password=shh&amp;url='+location.href;
    javascript:location.href='http://127.0.0.1:5000/add/'+window.location.href.replace(/^http(s?):\/\//i, "")
'''

#javascript:(function(){var list=prompt('Save to List');window.open('http://'+ list +'.saved.io/'+ document.location.href);})();
#javascript:(function(){var list=prompt('Save to List');window.open('http://127.0.0.1:5000/add/'+ document.location.href);})();
#javascript:(function(){window.open('http://127.0.0.1:5000/add/'+ document.location.href);})();
#take out https://
#https://stackoverflow.com/questions/43482152/how-can-i-remove-http-or-https-using-javascript
#window.location.href.replace(/^http(s?):\/\//i, "")


#can't cope with the /
#https://stackoverflow.com/questions/2992231/slashes-in-url-variables
#You can use encodeURIComponent and decodeURIComponent for this purpose. – Keavon Jun 26 '17 
# encodeURIComponent( document.location.href )
#javascript:location.href='http://127.0.0.1:5000/add/'+encodeURIComponent(window.location.href);


'''
javascript:(function(){
    location.href='http://127.0.0.1:5000/add/?url='+
    encodeURIComponent(window.location.href)+
    '&title='+encodeURIComponent(document.title)
})()
'''
'''
javascript:(function(){
    location.href='http://127.0.0.1:5000/add/'+
    encodeURIComponent(window.location.href)
})()
'''
#javascript:void(location.href="http://www.yacktrack.com/home?query="+encodeURI(location.href))
#javascript:void(location.href="http://127.0.0.1:5000/add?url="+encodeURI(location.href))
#javascript:void(location.href="http://127.0.0.1:5000/add/"+encodeURIComponent(location.href))
#https://gist.github.com/Nodja/34cfd28ba0e89a9bbcc3de604355b704
'''
javascript: 
            args = location.href;
            window.open("http://127.0.0.1:5500/youtubedl"
                       
                            + "&args="  + encodeURIComponent(args)
                        , '_blank');
'''
'''
javascript: 
            args = location.href;
            window.open("http://127.0.0.1:5000/add/"
                       
                            + "&args="  + encodeURIComponent(args)
                     );
'''
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

#javascript:location.href='http://127.0.0.1:5000/add/?password=shh&amp;url='+location.href;
#javascript:location.href='http://127.0.0.1:5000/add/?url='+location.href+'&title='+document.title;
@app.route('/add/', methods=["GET", "POST"])
@login_required
def add():
    page={}
    page['url']=request.args.get('url')
    page['title']=request.args.get('title')
    print(page)
    db.users.find_one_and_update({"_id": session['user_id']}, {"$push": {"saved_pages": page}})
    #user =db.users.find_one(({"_id": session['user_id']}))

    print('add route')
    #https://charlesleifer.com/blog/building-bookmarking-service-python-and-phantomjs/
    '''
    password = request.args.get('password')
    if password != PASSWORD:
        abort(404)
    '''
    #args = request.args.get('args', ""
    #)
    #title=request.args.get('title')
    url = request.args.get('url')
    #print(url)
    #print('title:' + title)
    #print(args)
    #a=url
    #print('xxxxxxxxxxx' + a)
    #return render_template('search.html')
    
    return redirect(url)
    '''
    if url:
        bookmark = Bookmark(url=url)
        bookmark.fetch_image()
        bookmark.save()
        return redirect(url)
    '''
'''
flask.debughelpers.FormDataRoutingRedirect

flask.debughelpers.FormDataRoutingRedirect: b'A request was sent to this URL (http://127.0.0.1:5000/page) 
but a redirect was issued automatically by the routing system to "http://127.0.0.1:5000/page/". 
 The URL was defined with a trailing slash so Flask will automatically redirect to the URL with the trailing slash if it was accessed without one.
   Make sure to directly send your POST-request to this URL since we can\'t make browsers or HTTP clients redirect with form data reliably or without user interaction.
   \n\nNote: this exception is only raised in debug mode'

'''
'''
@app.route('/page/', methods=["GET", "POST"])
#@login_required
def page():
    url = request.args.get('url')
    if request.method == "GET":
        url = request.args.get('url')
        return render_template('page.html', url=url)
    if request.method == 'POST':
        note = request.form['note']
        print(note)
        return render_template('page.html', url=url)
'''
'''
@app.route('/page/', methods=["GET", "POST"])
#@login_required
def page():
    #a=request.args.getlist()
    #print(a)
    #url = request.args.get('url')
    print('a')
    
    if request.method == "GET":
      #  url =decodeURIComponent(url)
        url = request.args.get('url')
        #url=url
        return render_template('page.html', url=url)
    if request.method == 'POST':
        url=request.path
        #url=request.form['url']
        note = request.form['note']
        print(note)
        print(url)
        return render_template('page.html', url=url)
'''
@app.route('/page/', methods=["GET", "POST"])
@login_required
def page():
    user =db.users.find_one(({"_id": session['user_id']}))
    if request.method == "GET":
        url = request.args.get('url')
        note=  db.notes.find_one({'$and': [{'url': url},{'author': user['username']}]})
        if note:
            return render_template('page.html', url=url, note=note)
        else:
            return render_template('page.html', url=url)
    if request.method == 'POST':
        #db.activities.find_one_and_update({"_id": ObjectId(activity_id)}, {"$set": {"published": True}})
        url=request.args.get('url')
        note={}
        note['url'] = request.args.get('url')
        body = note['body'] = request.form['note']
        note['author'] = user['username']
        author=user['username']
        #note['author'] = 
        #db.notes.find_one_and_update({'url':note['url']}, {'$set': {'body':note['body']}})
        #https://docs.mongodb.com/manual/reference/operator/query/and/
        #db.inventory.find( { $and: [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } )
        #db_request.append({'$and': [{'indoor': True}, {'outdoor': True}]})
        alreadyExists = db.notes.find_one({'$and': [{'url': url},{'author': author}]})
        if not alreadyExists:
            db.notes.insert(note)
            #  db.users.find_one_and_update({"_id": session['user_id']}, {"$push": {"saved_pages": page}})
            #?
            #user.update_one({'$push': {'notes': note['url']}})
            db.users.find_one_and_update(user, {'$push': {'notes': note['url']}})
        else:
            #unhashable type 'dict'
            # db.activities.find_one_and_update({"_id": ObjectId(activity_id)}, {"$set": {"published": True}})
            db.notes.update_one(alreadyExists, {'$set': {'body':body}})

        #print(note)
        #print(url)
        return render_template('page.html', url=url, note=note)

#javascript:location.href=http://127.0.0.1:5000/page/'+location.href
#encodeURIComponent(args)
#javascript:location.href=http://127.0.0.1:5000/page/'+encodeURIComponent(location.href)
#<iframe src="https://fr.wikipedia.org/wiki/Main_Page" width="640" height="480">

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
