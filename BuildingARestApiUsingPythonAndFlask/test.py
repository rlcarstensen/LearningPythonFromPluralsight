def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

valid_object = {
    "name": "f",
    "price": 6.99,
    "isbn": 1234567890
}

missing_name = {
    "price": 6.99,
    "isbn": 1234567890
}

missing_price = {
    "name": "f",
    "isbn": 1234567890
}

missing_isbn = {
    "name": "f",
    "price": 6.99,
}

empty_dictionary = {}

# from test import *
# validBookObject(valid_object)
# validBookObject(missing_name)
# validBookObject(missing_price)
# validBookObject(missing_isbn)
# validBookObject(empty_dictionary)
