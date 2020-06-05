from flask import Flask, jsonify, request

from Controllers.UserController import User
from Controllers.bookController import Book

app = Flask(__name__)


@app.route('/user/signup', methods=['POST'])  # routers for api
def signup():
    p_username = request.json['username']  # params from request body
    p_email = request.json['email']
    p_password = request.json['password']
    user = User()
    result = User.createuser(user, p_username, p_email, p_password)  # self missing
    return jsonify(
        id=result
    )


@app.route('/user/login', methods=['POST'])
def login():
    p_email = request.json['email']
    p_password = request.json['password']
    user = User()
    result = User.verifyUserExists(user, p_email, p_password)
    return jsonify(
        username=result[1],
        id=result[0]
    )


@app.route('/book/add', methods=['POST'])
def addBook():
    loginId = request.json['loginId']  # params from request body
    isbn = request.json['isbn']
    name = request.json['name']
    description = request.json['description']
    onCollection = request.json['onCollection']
    interested = request.json['interested']
    book = Book()
    result = Book.addMyBook(book, loginId, isbn, name, description, onCollection, interested)
    return jsonify(result)


@app.route('/book/update', methods=['POST'])
def updateBooks():
    loginId = request.json['loginId']  # params from request body
    isbn = request.json['isbn']
    onCollection = request.json['onCollection']
    interested = request.json['interested']
    book = Book()
    result = Book.updateMyBooks(book, loginId, isbn, onCollection, interested)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)  # Auto reload changes
