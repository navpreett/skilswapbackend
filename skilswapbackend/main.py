from flask import Flask, jsonify
from flask_cors import CORS
from routes.account.account import account_route

app = Flask(__name__)
CORS(app)


def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.after_request
def after_request(response):
    return add_cors_headers(response)


@app.route("/")
def hello_world():
    response = jsonify({"message": "Hello World!"})
    print("root route")
    return response


app.register_blueprint(account_route, url_prefix="/account")


if __name__ == "__main__":
    app.run(debug=True)
