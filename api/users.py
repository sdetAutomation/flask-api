import jsonschema

from schemas.user_schema import *
from flask import jsonify, Response, request, json
from models.user_model import User
from messages.error_messages import *


def get_users():
    return_value = jsonify({'users': User.get_all_users()})
    return return_value


def get_by_username(username):
    response = Response(str(User.get_user(username)), 200, mimetype="application/json")
    return response


def add_user():
    request_data = request.get_json()
    try:
        jsonschema.validate(request_data, add_user_schema)
        User.add_user(request_data['username'], request_data['email'])
        response = Response(json.dumps(request_data), 201, mimetype="application/json")
        response.headers['Location'] = "users/v1/" + str(request_data['username'])
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response


def update_email(username):
    request_data = request.get_json()
    try:
        jsonschema.validate(request_data, update_email_schema)
        # username is coming from url param, and email from json request body
        User.update_email(username, request_data['email'])
        response = Response('', 204, mimetype="application/json")
    except jsonschema.exceptions.ValidationError as exc:
        response = Response(error_message_helper(exc.message), 400, mimetype="application/json")
    return response


def delete_user(username):
    if User.delete_user(username):
        response = Response('', 204)
    else:
        response = Response(json.dumps(invalid_delete_error_msg_users), 404, mimetype="application/json")
    return response
