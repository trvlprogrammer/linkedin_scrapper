
from apps.api import bp
from flask import jsonify, request, current_app
from apps import api_response
import requests
from apps.linkedin_api.linkedin import Linkedin
from apps.api import utils
import time

@bp.route("/get_profile_data", methods=["POST"])
def get_profile_data():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    urls = request.json.get("urls", [])
    try :
        linkedin_api = Linkedin(username, password)
        data = []
        for url in urls:
            public_id = utils.get_linkedin_profile_id(url)
            profile = linkedin_api.get_profile(public_id)
            contact_info = linkedin_api.get_profile_contact_info(public_id)       
            data.append({**profile, **contact_info})
        response = api_response("success","Success get profile data by url", data)
        return jsonify(response)

    except Exception as e:
        print(e)
        response = api_response("error","Error get profile data by url", {})
        return jsonify(response)


@bp.route("/get_people_by_locations", methods=["POST"])
def get_people_by_locations():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    location = request.json.get("location", False)
    try :
        linkedin_api = Linkedin(username, password)        
        data = []
        start_time = time.time()
        if location:
            regions = linkedin_api.get_location_urn(location)
            print(divmod(time.time() - start_time,60))
            print("finished get regions urn id")
            profile_ids = linkedin_api.search_people(regions=regions)
            print(profile_ids)
            print(divmod(time.time() - start_time,60))
            print("finished search people")

            for profile_id in profile_ids:
                profile = linkedin_api.get_profile(profile_id["public_id"])
                print(divmod(time.time() - start_time,60))
                print("finished get profile")
                contact_info = linkedin_api.get_profile_contact_info(profile_id["public_id"])
                print(divmod(time.time() - start_time,60))
                print("finished get contact info")       
                data.append({**profile, **contact_info})

        response = api_response("success","Success get profile data by region", data)
        return jsonify(response)

    except Exception as e:
        print(e)
        response = api_response("error","get profile data by region", [])
        return jsonify(response)
