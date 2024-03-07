"""user's account."""

from flask import Blueprint, Response, jsonify

account_route = Blueprint("account_route", __name__)


@account_route.route("/", methods=["GET"])
def account_index() -> Response:
    """

    Account management route returning a JSON response.

    Returns:
        Response: The Flask response object.
    """
    return jsonify({"message": "Hello account management route!"})
