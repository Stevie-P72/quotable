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
@app.route('/get_quotes/<search_type>/<search_content>',
           methods=["GET", "POST"])
def get_quotes(search_type="", search_content=""):
    if search_type == "" and search_content == "":
        return render_template('timeline.html',
                               quotes=mongo.db.Quotes.find())
    else:
        quote_list = mongo.db.Quotes.find({'$text':
                                           {'$search': search_content}})
        if quote_list.count() == 0:
            return render_template('no_results.html')
        return render_template('timeline.html',
                               quotes=quote_list)


@app.route('/add_comment/<quote_id>', methods=["POST"])
def add_comment(quote_id):
    quote = mongo.db.Quotes.find_one({"_id": ObjectId(quote_id)})
    username = request.form.get('comment_user')
    comment = request.form.get('comment_content')
    if not username or not comment:
        return redirect(url_for('get_quotes'))
    else:
        try:
            comment_list = quote['comments']+[[username, comment]]
        except KeyError:
            comment_list = [[request.form.get('comment_user'),
                            request.form.get('comment_content')]]
        mongo.db.Quotes.update({"_id": ObjectId(quote_id)},
                               {"$set": {"comments": comment_list}})
        return redirect(url_for('get_quotes'))


@app.route('/new_post')
def new_post():
    return render_template('create_post.html')


@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    mongo.db.Quotes.remove({'_id': ObjectId(quote_id)})
    return redirect(url_for('get_quotes'))


@app.route('/upload_post', methods=["POST"])
def upload_post():
    quotes = mongo.db.Quotes
    quotes.insert_one(request.form.to_dict())
    return redirect(url_for('get_quotes'))


@app.route('/edit_quote/<quote_id>', methods=["POST"])
def edit_quote(quote_id):
    quote_to_edit = mongo.db.Quotes.find_one({"_id": ObjectId(quote_id)})
    comment_list = quote_to_edit["comments"]
    mongo.db.Quotes.update({'_id': ObjectId(quote_id)},
                           {'username': request.form.get('username'),
                            'quote': request.form.get('quote'),
                            'credit': request.form.get('credit'),
                            'comments': comment_list})
    return redirect(url_for('get_quotes'))


@app.route('/search_quotes', methods=["POST", "GET"])
def search_quotes():
    mongo.db.Quotes.drop_indexes()
    search_type = request.form.get('search_type')
    search_content = request.form.get('search_content')
    if search_content == "":
        return redirect(url_for('get_quotes'))
    if search_type == "all":
        mongo.db.Quotes.create_index([("username", 'text'),
                                      ("quote", 'text'),
                                      ("credit", 'text')],
                                     default_language='none')
    else:
        mongo.db.Quotes.create_index([(search_type, 'text')],
                                     default_language='none')
    return redirect(url_for('get_quotes',
                    search_type=search_type, search_content=search_content))


@app.route('/delete_comment/<quote_id>/<username>/<content>')
def delete_comment(quote_id, username, content):
    print(username)
    print(content)
    quote = mongo.db.Quotes.find_one({"_id": ObjectId(quote_id)})
    comment_list = quote['comments']
    comment_list.remove([username, content])
    mongo.db.Quotes.update({"_id": ObjectId(quote_id)},
                           {"$set": {"comments": comment_list}})
    return redirect(url_for('get_quotes'))


@app.route('/search_page')
def search_page():
    return render_template('search_page.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
