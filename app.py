import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'quotableDB'
MONGODB_URI = os.getenv("QUOTABLEURI")
