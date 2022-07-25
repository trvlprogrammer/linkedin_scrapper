
from apps.api import bp
from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required
from apps import api_response
from apps.utils import selenium_helper
import requests
from apps.utils.config_routes import Voyager_API

@jwt_required()
@bp.route("/detail_user", methods=["POST"])
def detail_user():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    cookies = selenium_helper.linkedin_get_cookies(username,password)
    url = Voyager_API.base_url + Voyager_API.voyager_me
    try :
        result = linkedin_get_helper(cookies,url)
        response = api_response("success","Success get user detail", result)
        return jsonify(response)
    except Exception as e:
        print(e)
        response = api_response("error","Error get user detail", {})
        return jsonify(response)


@jwt_required()
@bp.route("/network_info", methods=["POST"])
def network_info():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    cookies = selenium_helper.linkedin_get_cookies(username,password)
    user_id = get_entity_user_id(cookies)
    url = Voyager_API.base_url + Voyager_API.voyager_network_info%(user_id)
    try :
        result = linkedin_get_helper(cookies,url)
        response = api_response("success","Success get user network info", result)
        return jsonify(response)
    except Exception as e:
        print(e)
        response = api_response("error","Error get user network info", {})
        return jsonify(response)


@jwt_required()
@bp.route("/user_profile", methods=["POST"])
def user_profile():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    cookies = selenium_helper.linkedin_get_cookies(username,password)
    url = Voyager_API.base_url + Voyager_API.voyager_sso_you
    try :
        result = linkedin_get_helper(cookies,url)
        response = api_response("success","Success get user profile", result)
        return jsonify(response)
    except Exception as e:
        print(e)
        response = api_response("error","Error get user profile", {})
        return jsonify(response)

# function helper to get entity user_id
def get_entity_user_id(cookies):
    url = Voyager_API.base_url + Voyager_API.voyager_me
    result = linkedin_get_helper(cookies,url)
    return result["miniProfile"]["entityUrn"].strip('urn:li:fs_miniProfile:')


#helper get request function
def linkedin_get_helper(l_cookies,url):
    try :
        headers = {
            "user-agent":current_app.config["USER_AGENT"]
        }
        with requests.Session() as s:
            s.cookies['li_at'] = l_cookies["li_at"]
            s.cookies["JSESSIONID"] = l_cookies["JSESSIONID"]
            s.headers = headers
            s.headers["csrf-token"] = l_cookies["JSESSIONID"].strip('"')
            response = s.get(url)
            result = response.json()
            return result
    except Exception as e:
        print(e)
