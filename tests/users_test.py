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
    td_user = 'thor'
    response = client.get('/users/v1')
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_user not in json_info:
        print("FAIL: Not able to find td " + td_user)
        assert False


def test_tc0002_get_by_username(client):
    td_username = 'superman'
    response = client.get('/users/v1/' + td_username)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert response code
    assert response.status_code == 200
    # assert username is found on response json
    if td_username not in json_info:
        print("FAIL: Not able to find td " + td_username)
        assert False


def test_tc0003_post(client):
    td_username = 'batman'
    td_email = 'batman@gmail.com'

    response = client.post('/users/v1', data=json.dumps(dict(
        username=td_username,
        email=td_email
    )), mimetype='application/json')

    json_info = helper(response.response)

    if td_username not in json_info and td_email not in json_info:
        print("FAIL: Not able to find td " + td_username + ' ' + td_email)
        assert False


def test_tc0004_put(client):
    td_username = 'darth'
    td_email = 'luke@gmail.com'

    response = client.put('/users/v1/' + td_username, data=json.dumps(dict(email=td_email)),
                          mimetype='application/json')
    # assert proper status code returned
    assert response.status_code == 204
    # making a get call to retrieve record to verify email updated
    response = client.get('/users/v1/' + td_username)
    # using helper to format response json for assert
    json_info = helper(response.response)
    # assert email is found on response json
    if td_email not in json_info:
        print("FAIL: Not able to find td " + td_email)
        assert False


def test_tc0005_delete(client):
    td_username = 'delete'
    td_email = 'delete@gmail.com'
    # creating record for delete
    test = client.post('/users/v1', data=json.dumps(dict(
        username=td_username,
        email=td_email
    )), mimetype='application/json')

    response = client.delete('/users/v1/' + td_username)
    assert response.status_code == 204


def test_tc0006_bad_post(client):
    td_username = 'et'
    td_email = 'et@gmail.com'
    td_error_msg = '{\'error\': "\'username\' is a required property."}'

    response = client.post('/users/v1', data=json.dumps(dict(
        usernamez=td_username,
        email=td_email
    )), mimetype='application/json')

    assert response.status_code == 400

    json_info = str(helper(response.response))

    if td_error_msg not in json_info:
        print("FAIL: Error message not found: " + td_error_msg)
        assert False


def test_tc0007_bad_put(client):
    td_username = 'darth'
    td_email = 'luke@gmail.com'
    td_error_msg = '{\'error\': "\'email\' is a required property."}'

    response = client.put('/users/v1/' + td_username, data=json.dumps(dict(emailz=td_email)),
                          mimetype='application/json')
    # assert proper status code returned
    assert response.status_code == 400

    json_info = helper(response.response)
    # assert email is not found on response json
    if td_error_msg not in json_info:
        print("Error message not found: " + td_error_msg)
        assert False


def test_tc0008_bad_delete(client):
    td_username = 'loki'
    td_error_msg = '{\'error\': \'User not found, unable to delete.\'}'

    response = client.delete('/users/v1/' + td_username)

    # assert proper status code returned
    assert response.status_code == 404
    json_info = helper(response.response)
    # assert email is not found on response json
    if td_error_msg not in json_info:
        print("Error message not found: " + td_error_msg)
        assert False
