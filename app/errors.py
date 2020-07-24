from flask import render_template
from app import app

"""
Error handling
From :https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
"""
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404