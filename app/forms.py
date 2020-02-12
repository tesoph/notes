#Most Flask extensions use a flask_<name> naming convention for their top-level import symbol. 
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        '''
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    name = StringField('name' validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')
    '''
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


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#from app.models import User

def loginForm(loginform_):

        users=db.users
        loginform = loginform_
        user = users.find_one({"username": loginform['username']})
        if not user or not check_password_hash(user['password'], loginform['password']):
            flash('Invalid username or password')
            return render_template('login.html')
        else:
            session['user_id'] = user['_id']
            session['username']=user['username']
            userLoggedIn=True 
            return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
 