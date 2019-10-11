from flask import *
from app import app
from app.models import twitter
from flask import render_template, request, redirect

from flask_pymongo import PyMongo
# name of database
app.config['MONGO_DBNAME'] = 'gif_twitter_search'
# URI of database
#taken from mongodb website
app.config['MONGO_URI'] = 'mongodb+srv://admin:clustering@cluster0-gwaon.mongodb.net/gif_twitter_search?retryWrites=true&w=majority'
mongo = PyMongo(app)
@app.route('/')
@app.route('/index')
#CONNECT TO DB, ADD DATA
def index():
    #connect to database
    collection = mongo.db.results
    #query database for all events
    results = list(collection.find({}))
    #shows html file
    return render_template('index.html', results = results)
@app.route('/form')
def form():
    results = mongo.db.results
    #searches for all entries in the database
    results = list(results.find({}))
    #loads index.html
    return render_template('index.html', results = results)
@app.route('/results', methods=['GET','POST'])
def results():
    userdata= dict(request.form)
    gif_amount = userdata['quantity']
    username = userdata['name']
    email = userdata['email']
    #connects to the database
    results= mongo.db.results
    results.insert({'quantity':gif_amount, 'name':username, 'email':email})
    #searches for all entries in the database
    results = list(results.find({}))
    output = twitter.api_call()
    print(output)
    #loads index.html
    return render_template('results.html', results = results, username = username, quantity= gif_amount, email = email, output=output)
    print(userdata)
@app.route('/api_data',methods=['GET','POST'])
def api_data():
    api_data= dict(request.form)
    data = twitter.api_call(api_data)
    return render_template('form.html',data=data)
