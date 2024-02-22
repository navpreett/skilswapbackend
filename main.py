from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    response = jsonify({'message': 'Hello World!'})
    print("root route")
    return response


if __name__ == '__main__':
    app.run(debug=True)

