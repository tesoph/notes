from flask import render_template
from app import app

'''
A decorator modifies the function that follows it.
@app.route('/index') = when web browser requests the /index url,
Flask invokes this function and passes the return value back to the browser as a response
'''
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
     posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    '''
    The render_template() function invokes the Jinja2 template engine that comes bundled with the Flask framework. 
    Jinja2 substitutes {{ ... }} 
    blocks with the corresponding values, given by the arguments provided in the render_template() call.
    '''
    return render_template('index.html', title='Home', user=user, posts=posts)