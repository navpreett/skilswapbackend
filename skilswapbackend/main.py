"""Main file."""


from flask import Flask, Response, jsonify
from flask_cors import CORS

from skilswapbackend.routes.account.account import account_route

app = Flask(__name__)
CORS(app)


def add_cors_headers(response: Response) -> Response:
    """
    Add CORS headers to the response.

    Args:
        response (Response): The Flask response object.

    Returns:
        Response: The modified response object.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.after_request
def after_request(response: Response) -> Response:
    """
    After request hook to add CORS headers.

    Args:
        response (Response): The Flask response object.

    Returns:
        Response: The modified response object.
    """
    return add_cors_headers(response)


@app.route("/")
def hello_world() -> Response:
    """
    Root route returning a JSON response.

    Returns:
        Response: The Flask response object.
    """
    response = jsonify({"message": "Hello liqejfjlq!"})
    print("root route")
    return response


app.register_blueprint(account_route, url_prefix="/account")

if __name__ == "__main__":
    app.run(debug=True)
