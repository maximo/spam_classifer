# author: Rui Maximo

# create an empty file called conftest.py in the root directory
# for pytest to be able to resolve this module
from app import create_app

import pytest
import json

url = '/'

@pytest.fixture
def client():
    flask_app = create_app()
    client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello World!'

def test_non_spam(client):
    """
    GIVEN a Flask application
    WHEN the '/' or '/index' page is requested (POST) with non-spam content
    THEN check the response is valid
    """
    data = 'this is body content'
    response = client.post(
        url,
        data={'input':data})
    assert response.status_code == 200
    output = json.loads(response.data)
    assert output['output'] == 'ham'

def test_spam(client):
    """
    GIVEN a Flask application
    WHEN the '/' or '/index' page is requested (POST) with spam content
    THEN check the response is valid
    """
    data = 'please click on this link'
    response = client.post(
        url,
        data={'input':data})
    assert response.status_code == 200
    output = json.loads(response.data)
    assert output['output'] == 'spam'

def test_invalid_field(client):
    """
    GIVEN a Flask application
    WHEN the '/' or '/index' page is requested (POST) with an invalid parameter name
    THEN check the response is invalid
    """
    data = {'inputs': 'this is content'}
    response = client.post(url, json=data)
    assert response.status_code == 400

def test_missing_field(client):
    """
    GIVEN a Flask application
    WHEN the '/' or '/index' page is requested (POST) with null parameter and value
    THEN check the response is invalid
    """
    data = {'': ''}
    response = client.post(url, json=data)
    assert response.status_code == 400

def test_missing_value(client):
    """
    GIVEN a Flask application
    WHEN the '/' or '/index' page is requested (POST) with a null value
    THEN check the response is invalid
    """
    data = {'input': ''}
    response = client.post(url, json=data)
    assert response.status_code == 200
    output = json.loads(response.data)
    assert output['output'] == 'ham'
