import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'quotableDB'
app.config["MONGO_URI"] = os.getenv("QUOTABLEURI")
mongo = PyMongo(app)


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Connected to Mongo")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Connection Failure: %S") % e


@app.route('/')
@app.route('/get_quotes')
def get_quotes():
    return render_template('timeline.html', quotes=mongo.db.Quotes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
