import json
import os
import connexion
import pytest

from config import my_app
from db_config import db

flask_app = connexion.FlaskApp(__name__)
# setting in memory database for testing
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(my_app.root_path, 'database/test.db')
flask_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
flask_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(flask_app.app)
flask_app.add_api('../swagger/swagger.yml')


@pytest.fixture(scope='module')
def client():
    with flask_app.app.test_client() as c:
        yield c


@pytest.fixture(scope='module')
def helper(json_info):
    for info in json_info:
        first_row = info.decode("utf-8")
        return str(json.loads(first_row))


def test_tc0001_get(client):
    td_state = 'mn'
    response = client.get('/locations/v1')
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert location is found on response json
    if td_state not in json_info:
        print("FAIL: Not able to find td " + td_state)
        assert False


def test_tc0002_get_by_location(client):
    td_location = 'ca'
    response = client.get('/locations/v1/' + td_location)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert location is found on response json
    if td_location not in json_info:
        print("FAIL: Not able to find td " + td_location)
        assert False


def test_tc0003_post(client):
    td_state = 'wi'
    td_capital = 'madison'

    response = client.post('/locations/v1', data=json.dumps(dict(
        state=td_state,
        capital=td_capital
    )), mimetype='application/json')

    json_info = helper(response.response)

    if td_state not in json_info and td_capital not in json_info:
        print("FAIL: Not able to find td " + td_state + ' ' + td_capital)
        assert False


def test_tc0004_put(client):
    td_state = 'ny'
    td_capital = 'new capital for new york'

    response = client.put('/locations/v1/' + td_state, data=json.dumps(dict(capital=td_capital)),
                          mimetype='application/json')
    # assert proper status code returned
    assert response.status_code == 204
    # making a get call to retrieve record to verify email updated
    response = client.get('/locations/v1/' + td_state)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert email is found on response json
    if td_capital not in json_info:
        print("FAIL: Not able to find td " + td_capital)
        assert False


def test_tc0005_delete(client):
    td_state = 'delete'
    td_capital = 'delete_capital'
    # creating record for delete
    test = client.post('/locations/v1', data=json.dumps(dict(
        state=td_state,
        capital=td_capital
    )), mimetype='application/json')

    response = client.delete('/locations/v1/' + td_state)
    assert response.status_code == 204


def test_tc0006_bad_post(client):
    td_state = 'wi'
    td_capital = 'madison'
    td_error_msg = '{\'error\': "\'state\' is a required property."}'

    response = client.post('/locations/v1', data=json.dumps(dict(
        statez=td_state,
        capital=td_capital
    )), mimetype='application/json')

    assert response.status_code == 400

    json_info = str(helper(response.response))

    if td_error_msg not in json_info:
        print("FAIL: Error message not found: " + td_error_msg)
        assert False


def test_tc0007_bad_put(client):
    td_state = 'wi'
    td_capital = 'madison'
    td_error_msg = '{\'error\': "\'capital\' is a required property."}'

    response = client.put('/locations/v1/' + td_state, data=json.dumps(dict(capitalz=td_capital)),
                          mimetype='application/json')
    # assert proper status code returned
    assert response.status_code == 400

    json_info = helper(response.response)
    # assert capital is not found on response json
    if td_error_msg not in json_info:
        print("Error message not found: " + td_error_msg)
        assert False


def test_tc0008_bad_delete(client):
    td_state = 'ut'
    td_error_msg = '{\'error\': \'Location not found, unable to delete.\'}'

    response = client.delete('/locations/v1/' + td_state)

    # assert proper status code returned
    assert response.status_code == 404
    json_info = helper(response.response)

    print(json_info)
    print(td_error_msg)

    # assert email is not found on response json
    if td_error_msg not in json_info:
        print("Error message not found: " + td_error_msg)
        assert False
