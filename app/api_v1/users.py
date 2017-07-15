

from flask import Blueprint, jsonify
from flask_login import current_user, login_required

from app import app
from app.schemas.schemas import user_schema

mod = Blueprint("default", __name__, url_prefix="/api")


@app.route("/whoami", methods=["GET"])
def who_am_i():
    if current_user.is_authenticated:
        name = current_user.name
    else:
        name = "anonymous"
    return jsonify({"name": name})


@app.route("/profile", methods=["GET"])
@login_required
def user_profile():
    return user_schema.jsonify(current_user)
