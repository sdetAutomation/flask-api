import jsonschema

from schemas.location_schema import *
from flask import jsonify, Response, request, json
from models.location_model import Location
from messages.error_messages import *


def get_locations():
    return_value = jsonify({'locations': Location.get_all_locations()})
    return return_value


def get_by_state(state):
    response = Response(str(Location.get_location(state)), 200, mimetype="application/json")
    return response


def add_location():
    request_data = request.get_json()
    try:
        jsonschema.validate(request_data, add_location_schema)
        Location.add_location(request_data['state'], request_data['capital'])
        response = Response(json.dumps(request_data), 201, mimetype="application/json")
        response.headers['Location'] = "locations/v1/" + str(request_data['state'])
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response


def update_capital(state):
    request_data = request.get_json()
    try:
        jsonschema.validate(request_data, update_capital_schema)
        # state is coming from url param, and capital from json request body
        Location.update_capital(state, request_data['capital'])
        response = Response('', 204, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response


def delete_location(state):
    if Location.delete_location(state):
        response = Response('', 204)
    else:
        response = Response(json.dumps(invalid_delete_error_msg_locations), 404, mimetype="application/json")
    return response
