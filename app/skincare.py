import os
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


def search_skincare():
    # POST route
    ingredientSearch=False
    brandSearch=False
    if request.method == "POST":
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "data", "products.json")
        # data = json.load(open(json_url))
        with open(json_url, "r") as read_file:
            data = json.load(read_file)
        print(type(data))
        # print(data[:2])
        for c in data[:5]:
            print(c['brand'])
        # pageContent = []
        ingredientSearchTerm = request.form.get('ingredientSearchTerm')
        brandSearchTerm = request.form.get('brandSearchTerm')
        il = []
        bl = []
        if ingredientSearchTerm:
            ingredientSearch=True
            for i in data:
                if ingredientSearchTerm in i['ingredient_list']:
                 # print(i)
                      il.append(i)
        if brandSearchTerm:
            brandSearch=True
            for i in data:
                if brandSearchTerm in i['brand']:
                     bl.append(i)
        # render list
        #print(l)
        return render_template('skincare.html', il=il, bl=bl,ingredientSearch=ingredientSearch, brandSearch=brandSearch)
    # GET route
    else:
        return render_template('search_skincare.html')

    # GET /product?q=rose+water
    # https://skincare-api.herokuapp.com/product?q=rose&limit=25&page=1
    '''
    filename = os.path.join(app, 'data', 'products.json')
    with open(filename) as f:
             d= json.load(f)
             '''
    # https://stackoverflow.com/questions/21133976/flask-load-local-json