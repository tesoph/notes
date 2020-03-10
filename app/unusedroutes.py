

@app.route('/notemaker')
def notemaker():
    form = NoteForm()
    return render_template('page2.html', title='Make Note', form=form)


'''
Bookmarklet #2
Clicking the bookmarklet opens a notepad on the wiki page
'''
@app.route('/page3/', methods=["GET", "POST"])
# @login_required
def page3():

    #user = db.users.find_one(({"_id": session['user_id']}))

    if request.method == "GET":
        print('getting')
        url = request.args.get('url')
        # url=note_url
        #title = request.args.get('title')
        # note = db.notes.find_one(
        #    {'$and': [{'url': url}, {'author': user['username']}]})
        # if note:
        #   public=note['public']
        #   public=str(public)
        #   print('note exists, is it public or private?' + str(public))
        #   return render_template('page.html', url=url, note=note, title=title, public=public)
       # else:
        #   public=False
        #   public=str(public)
        return render_template('page.html', url=url, title='my title', public=True)

    if request.method == 'POST':
        print('posting')
        # https://stackoverflow.com/questions/25491090/how-to-use-python-to-execute-a-curl-command
        # https://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url/13921930#13921930
        #url = request.values.get('url')
        url = request.values.get('url')
        val = str(dict(request.values))
        print('vALS;'+val)
        note = {}
        data2 = request.form['n']
        note['body'] =request.form['n']
        note['url']=request.values.get('url')
        note['author']='Anon'
        note['public']=True
        #db.notes.insert(note)
        return redirect(url)


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
    '''930 536
    if request.method == "GET":
        url = request.args.get('url')
        title = request.args.get('title')
        note=  db.notes.find_one({'$and': [{'url': url},{'author': user['username']}]})
        if note:
            return render_template('page.html', url=url, note=note,title=title)
        else:
            return render_template('page.html', url=url)

    if request.method == 'POST':
 
        # https://stackoverflow.com/questions/25491090/how-to-use-python-to-execute-a-curl-command
        # https://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url/13921930#13921930
        url= request.values.get('url')
        response=requests.post(url)
        resp=response.text
        html_doc=resp
        soup = BeautifulSoup(html_doc, 'html.parser')
        print('soup title:' + soup.title.string)
 
        note={}
        
        print('asdsad' + url)
        # print('title' + request.values.get('title'))
        note['url'] = request.values.get('url')
        note['title'] = soup.title.string
        # note['title']=request.values.get('title')
        # note['url'] = request.args.get('url')
       # note['title']=request.args.get('title')
        body = note['body'] = request.form['note']
        # title = note['title'] = request.form['title']
        note['author'] = user['username']
        author=user['username']
        # note['author'] = 
        # db.notes.find_one_and_update({'url':note['url']}, {'$set': {'body':note['body']}})
        # https://docs.mongodb.com/manual/reference/operator/query/and/
        # db.inventory.find( { $and: [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } )
        # db_request.append({'$and': [{'indoor': True}, {'outdoor': True}]})
        alreadyExists = db.notes.find_one({'$and': [{'url': url},{'author': author}]})
        if not alreadyExists:
            print('not alreadyexists')
            print('note:' + note['body'])
            db.notes.insert(note)
            #  db.users.find_one_and_update({"_id": session['user_id']}, {"$push": {"saved_pages": page}})
            # ?
            # user.update_one({'$push': {'notes': note['url']}})
            db.users.find_one_and_update(user, {'$push': {'notes': note['url']}})
        else:
            print('does exists already')
            # unhashable type 'dict'
            # db.activities.find_one_and_update({"_id": ObjectId(activity_id)}, {"$set": {"published": True}})
            db.notes.update_one(alreadyExists, {'$set': {'body':body}})
            ''' ''' response = jsonify(data)''''''
            # print('note:' + note)

        # print(note)
        # print(url)
        return render_template('page.html', url=url, note=note)
        '''


@app.route('/page2/<note_url>', methods=["GET", "POST"])
@login_required
def page2(note_url):

    user = db.users.find_one(({"_id": session['user_id']}))

    if request.method == "GET":

        url = note_url
        note = db.notes.find_one(
            {'$and': [{'url': url}, {'author': user['username']}]})
        if note:
            return render_template('page.html', url=url, note=note)
        else:
            return render_template('page.html', url=url)

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

        print('asdsad' + url)
        # print('title' + request.values.get('title'))
        note['url'] = request.values.get('url')
        note['title'] = soup.title.string
        # note['title']=request.values.get('title')
        # note['url'] = request.args.get('url')
       # note['title']=request.args.get('title')
        body = note['body'] = request.form['note']
        # title = note['title'] = request.form['title']
        note['author'] = user['username']
        author = user['username']
        # note['author'] =
        # db.notes.find_one_and_update({'url':note['url']}, {'$set': {'body':note['body']}})
        # https://docs.mongodb.com/manual/reference/operator/query/and/
        # db.inventory.find( { $and: [ { price: { $ne: 1.99 } }, { price: { $exists: true } } ] } )
        # db_request.append({'$and': [{'indoor': True}, {'outdoor': True}]})
        alreadyExists = db.notes.find_one(
            {'$and': [{'url': url}, {'author': author}]})
        if not alreadyExists:
            print('not alreadyexists')
            print('note:' + note['body'])
            db.notes.insert(note)
            #  db.users.find_one_and_update({"_id": session['user_id']}, {"$push": {"saved_pages": page}})
            # ?
            # user.update_one({'$push': {'notes': note['url']}})
            db.users.find_one_and_update(
                user, {'$push': {'notes': note['url']}})
        else:
            print('does exists already')
            # unhashable type 'dict'
            # db.activities.find_one_and_update({"_id": ObjectId(activity_id)}, {"$set": {"published": True}})
            db.notes.update_one(alreadyExists, {'$set': {'body': body}})
            '''  response = jsonify(data)'''
            # print('note:' + note)

        # print(note)
        # print(url)
        return render_template('page.html', url=url, note=note)

    '''
<p>
    <a href='javascript:(function()%7Bconsole.log(%22bookmarklet%20starting%22)%3Bvar%20url%3Dlocation.href%3Bvar%20title%3Ddocument.title%3Bh%3D'wiki-note.herokuapp.com%2Fpage3%2F%3Furl%3D'%3Bvar%20element%20%3D%20document.getElementById('bodyContent')%3Bvar%20parent%20%3D%20element.parentNode%3Bvar%20wrapper%20%3D%20document.createElement('div')%3Bvar%20c%20%3D%20document.createElement('FORM')%3Bvar%20note%20%3D%20document.createElement('textarea')%3Bc.setAttribute('action'%2C%20h%2Burl)%3Bc.setAttribute('method'%2C%20'POST')%3Bwrapper.setAttribute(%22id%22%2C%20%22w%22)%3Bnote.setAttribute(%22id%22%2C%20%22n%22)%3Bnote.setAttribute('name'%2C%20'n')%3Bif(typeof%20nbody%20!%3D%3D%20'undefined')%7Bnote.innerHTML%20%3D%20nbody%3B%20%20%20%20%7Dc.setAttribute(%22id%22%2C%20%22c%22)%3Bc.appendChild(note)%3Bparent.replaceChild(wrapper%2C%20element)%3Bwrapper.appendChild(element)%3Bwrapper.appendChild(c)%3Bvar%20btn%20%3D%20document.createElement(%22BUTTON%22)%3Bbtn.setAttribute('type'%2C%20'submit')%3Bbtn.innerHTML%20%3D%20%22CLICK%20ME%22%3Bc.appendChild(btn)%3Bvar%20style%20%3D%20document.createElement('style')%3Bstyle.innerHTML%20%3D%20%60%23w%20%7B%7D%23bodyContent%7Bwidth%3A60%25%3B%7D%23c%7Btop%3A%2015%25%3Bwidth%3A%2035%25%3Bheight%3A%2080vh%3Bbackground-color%3A%20blue%3Bposition%3A%20fixed%3Bright%3A%200%3B%7D%23note%7Bwidth%3A100%25%3Bmin-height%3A90%25%3Boverflow-y%3Ascroll%3B%7D%60%3Bdocument.head.appendChild(style)%7D)()'>Note2</a>
    : note on wiki page</p>
    '''