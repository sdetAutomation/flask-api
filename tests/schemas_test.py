import json
import jsonschema

from schemas.location_schema import add_location_schema, update_capital_schema
from schemas.user_schema import add_user_schema, update_email_schema


def test_schema_tc0001_add_user_schema():
    td_post_body = '{ "email": "string", "username": "string" }'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_user_schema)


def test_schema_tc0002_update_email_schema():
    td_post_body = '{ "email": "string" }'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), update_email_schema)


def test_schema_tc0003_add_location_schema():
    td_post_body = '{ "capital": "string", "state": "string" }'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), add_location_schema)


def test_schema_tc0004_update_capital_schema():
    td_post_body = '{ "capital": "string" }'
    # json.loads converts string to json object
    jsonschema.validate(json.loads(td_post_body), update_capital_schema)