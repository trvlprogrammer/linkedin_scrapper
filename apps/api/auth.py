

from urllib import response
from apps.api import bp
from flask import jsonify, request, current_app
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, get_jwt_identity, jwt_required, current_user
from datetime import timedelta, timezone, datetime
from apps import api_response



@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == current_app.config["SCRAPER_USERNAME"] and password == current_app.config["SCRAPER_PASSWORD"]:
        access_token = create_access_token(username)
        refresh_token = create_refresh_token(username)
        response = api_response("success","Login Success",
            {
                "access_token" : access_token,
                "refresh_token" : refresh_token
            }
        )
        return jsonify(response)
    response = api_response("success","Username or password invalid",{})
    return jsonify(response), 401






