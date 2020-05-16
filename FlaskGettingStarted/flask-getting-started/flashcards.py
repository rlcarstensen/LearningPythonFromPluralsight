from flask import Flask, render_template, abort, jsonify, request
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template(
        "welcome.html",
        cards=db
    )
    # return "Welcome to my FlashCard application"


@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template('card.html', card=card, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route('/add-card', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        card = {
            'question': request.form['question'],
            'answer': request.form['answer']
        }
    else:
        return render_template('add_card.html')


@app.route('/api/card/')
def api_card_list():
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

# from datetime import datetime
# initial examples
# @app.route('/date')
# def date():
#     return "This page was served at " + str(datetime.now())

# counter = 0

# @app.route('/count-views')
# def count_views():
#     global counter
#     counter += 1
#     return 'This page was served ' + str(counter) + ' times'


# command line (bash) (in windows set can replace export)
# location of application to run
# export FLASK_APP=flashcards.py
# type of environment to run
# export FLASK_ENV=development
# flask run

# import flashcards
# flashcards.app.url_map
