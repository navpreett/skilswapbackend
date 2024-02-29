from flask import Blueprint, jsonify

account_route = Blueprint("account_route", __name__)


@account_route.route("/", methods=["Get"])
def account_index():
    return jsonify({"message": "Hello account management route!"})
