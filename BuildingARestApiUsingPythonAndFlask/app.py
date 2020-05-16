import datetime
import json
import jwt

from BookModel import *
from UserModel import User
from settings import *
from functools import wraps

app.config['SECRET_KEY'] = 'meow'

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return wrapper


@app.route('/login', methods=['POST'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])

    match = User.username_password_match(username, password)

    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
        return token
    else:
        return Response('', 401, mimetype='application/json')

# replaced in settings.py
# app = Flask(__name__)
# print(__name__)

# books = [
#     {
#         'name': 'Green Eggs and Ham',
#         'price': 7.99,
#         'isbn': 978039400165
#     },
#     {
#         'name': 'The Cat In The Hat',
#         'price': 6.99,
#         'isbn': 9782371000193
#     },
#     {
#         'name': 'A',
#         'price': 7.99,
#         'isbn': 9780394800165
#     }
# ]


@app.route('/')
def hello_world():
    return 'Hello World!'


# Get /books
# to change add "methods=['POST']" to .route()
@app.route('/books')
@token_required
def get_books():
    # return jsonify({'books': books})
    return jsonify({'books': Book.get_all_books()})


# POST /books
# {
#     'name': 'f',
#     'price': 6.99,
#     'isbn': 0123456789
# }


def validBookObject(bookObject):
    if "name" in bookObject and "price" in bookObject and "isbn" in bookObject:
        return True
    else:
        return False


@app.route('/books', methods=['POST'])
@token_required
def add_book():
    request_data = request.get_json()
    if validBookObject(request_data):
        # new_book = {
        #     "name": request_data['name'],
        #     "price": request_data['price'],
        #     "isbn": request_data['isbn']
        # }
        # books.insert(0, new_book)
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = '/books/' + str(request_data['isbn'])
        return response
    else:
        invalidBookObjectErrorMessage = {
            'error': 'Invalid book object passed in request',
            'helpString': 'Should have name, price, and isbn'
        }
        response = Response(json.dumps(invalidBookObjectErrorMessage), status=400, mimetype="application/json")
        return response


@app.route('/books/<int:isbn>')
@token_required
def get_book_by_isbn(isbn):
    # return_value = {}
    # print(type(isbn))
    # for book in books:
    #     if book['isbn'] == isbn:
    #         return_value = {
    #             'name': book['name'],
    #             'price': book['price']
    #         }
    return_value = Book.get_book(isbn)
    return jsonify(return_value)


def valid_put_request_data(bookObject):
    if "name" in bookObject and "price" in bookObject:
        return True
    else:
        return False


# PUT /books/31283127312
# {
#     'name': 'The Odyssey',
#     'price': 0.99
# }
@app.route('/books/<int:isbn>', methods=['PUT'])
@token_required
def replace_book(isbn):
    request_data = request.get_json()
    if not valid_put_request_data(request_data):
        invalidBookObjectErrorMessage = {
            'error': 'Invalid book object passed in request',
            'helpString': 'Should have name, price'
        }
        response = Response(json.dumps(invalidBookObjectErrorMessage), status=400, mimetype="application/json")
        return response

    # new_book = {
    #     'name': request_data['name'],
    #     'price': request_data['price'],
    #     'isbn': isbn
    # }
    # i = 0
    # for book in books:
    #     currentIsbn = book['isbn']
    #     if currentIsbn == isbn:
    #         books[i] = new_book
    #     i += 1
    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response("", status=204)
    return response


@app.route('/books/<int:isbn>', methods=['PATCH'])
@token_required
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if 'name' in request_data:
        Book.update_book_name(isbn, request_data['name'])
        # updated_book['name'] = request_data['name']
    if 'price' in request_data:
        Book.update_book_price(isbn, request_data['price'])
        # updated_book['price'] = request_data['price']
    # for book in books:
    #     if book['isbn'] == isbn:
    #         book.update(updated_book)
    response = Response('', status=204)
    response.headers['Location'] = '/books/' + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def delete_book(isbn):
    # i = 0
    # for book in books:
    #     if book['isbn'] == isbn:
    #         books.pop(i)
    #         response = Response("", status=204)
    #         return response
    #     i += 1
    if Book.delete_book(isbn):
        response = Response("", status=204)
        return response
    response = Response("book not found", status=404, mimetype='application/json')
    return response


app.run(port=5000)

# to run use 'python app.py'
