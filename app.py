from flask import Flask, jsonify, request

from Controllers.UserController import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify("hello py api auto reaload 2")


@app.route('/user/signup', methods=['POST'])  # routers for api
def signup():
    p_username = request.json['username']  # params from request body
    p_email = request.json['email']
    p_password = request.json['password']
    result = User.createuser(p_username, p_email, p_password)  # self missing
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)  # Auto reload changes
