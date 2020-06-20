import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'quotableDB'
app.config["MONGO_URI"] = os.getenv("QUOTABLEURI")
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_quotes', methods=["GET", "POST"])
def get_quotes():
    return render_template('timeline.html', quotes=mongo.db.Quotes.find())


@app.route('/add_comment/<quote_id>', methods=["POST"])
def add_comment(quote_id):
    quote = mongo.db.Quotes.find_one({"_id": ObjectId(quote_id)})
    try:
        comment_list = quote['comments']+[[request.form.get('comment_user'),
                                          request.form.get('comment_content')]]
    except KeyError:
        comment_list = [[request.form.get('comment_user'),
                        request.form.get('comment_content')]]
    mongo.db.Quotes.update({"_id": ObjectId(quote_id)},
                           {"$set": {"comments": comment_list}})
    print(quote)
    return redirect(url_for('get_quotes'))


@app.route('/new_post')
def new_post():
    return render_template('create_post.html')


@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    print(quote_id)
    mongo.db.Quotes.remove({'_id': ObjectId(quote_id)})
    return redirect(url_for('get_quotes'))


@app.route('/upload_post', methods=["POST"])
def upload_post():
    quotes = mongo.db.Quotes
    quotes.insert_one(request.form.to_dict())
    return redirect(url_for('get_quotes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
