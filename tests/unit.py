# author: Rui Maximo

import pytest
from app import app

@pytest.fixture
def client():
    micro_service = app.app()
    micro_service.debug = True
    client = micro_service.test_client()
    ctx = micro_service.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_valid_field(client):
    data = {'input': 'this is content'}
    response = client.post('/', json=data)
    assert response.status_code == 200

def test_invalid_field(client):
    data = {'inputs': 'this is content'}
    response = client.post('/', json=data)
    assert response.status_code == 400

def test_missing_field(client):
    data = {'': ''}
    response = client.post('/', json=data)
    assert response.status_code == 400

def test_missing_value(client):
    data = {'input': ''}
    response = client.post('/', json=data)
    assert response.status_code == 400